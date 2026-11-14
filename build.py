#!/usr/bin/env python3
import os
import pathlib
import shutil
import datetime
import yaml
import markdown

ROOT = pathlib.Path(__file__).parent
CONTENT_DIR = ROOT / "content"
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"
PUBLIC_DIR = ROOT / "public"
SITE_URL = "https://daynum.github.io"

def load_template(name):
    return (TEMPLATES_DIR / name).read_text(encoding="utf-8")

def parse_markdown_with_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        _, fm_text, body = text.split("---", 2)
        meta = yaml.safe_load(fm_text) or {}
        content_md = body.strip()
    else:
        meta = {}
        content_md = text
    html = markdown.markdown(
        content_md,
        extensions=["fenced_code", "codehilite"]
    )
    return meta, html

def slug_from_filename(path):
    return path.stem  # "hello-world.md" -> "hello-world"

def parse_date_for_sort(date_value):
    """Turn a frontmatter date into a datetime for sorting (supports dd/mm/yyyy)."""
    if isinstance(date_value, datetime.datetime):
        return date_value
    if isinstance(date_value, datetime.date):
        return datetime.datetime.combine(date_value, datetime.time())
    if isinstance(date_value, str):
        date_str = date_value.strip()
        for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d", "%Y/%m/%d"):
            try:
                return datetime.datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        try:
            return datetime.datetime.fromisoformat(date_str)
        except ValueError:
            return None
    return None

def build():
    # prepare output dir
    if PUBLIC_DIR.exists():
        shutil.rmtree(PUBLIC_DIR)
    PUBLIC_DIR.mkdir(parents=True)

    # copy static files
    out_static = PUBLIC_DIR / "static"
    shutil.copytree(STATIC_DIR, out_static)

    base_tpl = load_template("base.html")
    post_tpl = load_template("post.html")
    index_tpl = load_template("index.html")

    posts_meta = []
    year = datetime.date.today().year

    posts_out_dir = PUBLIC_DIR / "posts"
    posts_out_dir.mkdir()

    def render_page(title, content, depth):
        """Insert common template fields and correct relative paths."""
        static_prefix = "../" * depth
        home_link = f"{static_prefix}index.html"
        return (base_tpl.replace("%%TITLE%%", title)
                        .replace("%%CONTENT%%", content)
                        .replace("%%YEAR%%", str(year))
                        .replace("%%STATIC_PREFIX%%", static_prefix)
                        .replace("%%HOME_LINK%%", home_link))

    # build each post
    for md_file in sorted(CONTENT_DIR.glob("*.md")):
        meta, post_html = parse_markdown_with_frontmatter(md_file)
        slug = slug_from_filename(md_file)
        title = meta.get("title", slug)
        date = meta.get("date", "")
        # YAML can parse ISO dates into datetime objects; normalize to string for templating/sorting.
        if isinstance(date, (datetime.date, datetime.datetime)):
            date = date.isoformat()
        sort_date = parse_date_for_sort(date)

        body = post_tpl.replace("%%POST_TITLE%%", title)\
                       .replace("%%POST_DATE%%", date)\
                       .replace("%%POST_CONTENT%%", post_html)

        page = render_page(title, body, depth=1)

        out_path = posts_out_dir / f"{slug}.html"
        out_path.write_text(page, encoding="utf-8")

        posts_meta.append({
            "title": title,
            "date": date,
            "slug": slug,
            "sort_date": sort_date,
        })

    # sort posts by date desc (if date is present)
    posts_meta.sort(key=lambda p: p["sort_date"] or datetime.datetime.min, reverse=True)

    # build index.html
    items_html = []
    for p in posts_meta:
        items_html.append(
            f'<li><span class="post-date">{p["date"]}</span>'
            f'<a class="post-link" href="posts/{p["slug"]}.html">{p["title"]}</a></li>'
        )
    index_body = index_tpl.replace("%%POST_ITEMS%%", "\n".join(items_html))

    index_page = render_page("Home", index_body, depth=0)

    (PUBLIC_DIR / "index.html").write_text(index_page, encoding="utf-8")

    # sitemap.xml + robots.txt so search engines can find every post
    urls = [f"  <url><loc>{SITE_URL}/</loc></url>"]
    for p in posts_meta:
        lastmod = f"<lastmod>{p['sort_date']:%Y-%m-%d}</lastmod>" if p["sort_date"] else ""
        urls.append(f"  <url><loc>{SITE_URL}/posts/{p['slug']}.html</loc>{lastmod}</url>")
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "\n".join(urls) + "\n</urlset>\n")
    (PUBLIC_DIR / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (PUBLIC_DIR / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")

    print("Built site into", PUBLIC_DIR)

if __name__ == "__main__":
    build()
