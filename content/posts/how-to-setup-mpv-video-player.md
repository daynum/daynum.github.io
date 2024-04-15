+++
title = 'How to Setup Mpv Video Player'
date = 2023-11-20T09:00:00+05:30
draft = false
+++

## Why MPV and not VLC?
VLC is almost trash because, it:

- Uses the wrong matrix for RGB conversion (colors shown are wrong)
- Introduces strong banding
- Wrong chroma location
- Deinterlacing is broken
- Subtitle render is pretty old and breaks in heavy typesetting situations (in short, it shits when it comes to good anime subs)
- Stops to build font cache at the start of each file with new fonts (we’ve seen it, right?).
- It corrupts the video decoding if it takes too long to decode a single frame. Other players just skip the frame.

Comparison:  
- [https://slow.pics/c/XhbmrYgU](https://slow.pics/c/XhbmrYgU)  
- [https://slow.pics/c/95VZsDMs](https://slow.pics/c/95VZsDMs)  

Alright, now that VLC is out of the scene. Let’s see how to set up MPV.

If it’s your first time, MPV might seem a bit complex. It has a minimalistic GUI (it isn’t a GUI, technically).  
It is mainly controlled with a keyboard. But good people have made some modified versions of MPV, which can be beginner-friendly, giving a  "VLC" like interface.  
Because I will be talking about the OG one, I won’t go into much details about the other MPV mods, but here are the links to a few good ones you can try if you don’t want to go ahead with a bit of effort setting it up. But trust me, it’s worth it.

1. Mpv.net - [https://github.com/stax76/mpv.net](https://github.com/stax76/mpv.net)
2. Mpv easy player - [https://github.com/422658476/MPV-EASY-Player](https://github.com/422658476/MPV-EASY-Player)
3. Mpc-qt - [https://github.com/mpc-qt/mpc-qt](https://github.com/mpc-qt/mpc-qt)

## Getting started with our MPV
Instructions here are for the Windows platform. For Mac or Linux, they shouldn’t be too different.

1. First of all, go to [mpv.io](https://mpv.io) to download mpv.
2. In the Windows section, there are many builds given - third parties make them.
3. I use Shinchiro’s build from Sourceforge. It’s easier to update, and I haven’t tried others.
4. Download the latest zip file according to your architecture (32-bit or 64-bit).
5. Extract the zip file (you’ll need [7zip](https://www.7-zip.org/) for that).
6. We’ll call this folder just extracted as `mpv-root`.

Now, you can run your video files with mpv.exe.  
There is no  "installation" here. However, to make life easier, there’s a script inside the `mpv-root >> installer >> install.bat / mpv-install.bat`.  
Run this file with **admin privileges**, and it will associate the file types with mpv. And you’re done. Right-click on any video file and open it with mpv.

## Controlling MPV
MPV is majorly controlled with the keyboard bindings, which you can change as per your needs.  
A map of default key bindings can be found in `mpv-root >> doc >> mpbindings.png`.  
I suggest keeping this image handy on your desktop; it’ll be much easier to find the key bindings whenever needed, and you’ll learn them quickly.

## Configuring MPV
You can configure your mpv with two config files:

1.  Mpv.conf (configures the core mpv)
2.  Input.conf (configures the custom keybindings)

I haven’t used input.conf much, because default bindings are fine for me.

To use them, create a sub-directory named _ "portable\_config"_ (exact name) in the `mpv-root` directory. Inside _ "portable\_config"_ create two files - `mpv.conf` and `input.conf`.

Now, there are many options you can set in your `mpv.conf` to tailor it to your needs; even I don’t know all of them, I’ll just paste my conf file with comments and link to a few good confs so you can set the options as you want them.

My config:
{{< highlight bash "linenos=table,linenostart=1" >}}

#set the default volume to 100, max to 120
volume=100
volume-max=120

#keep mpv open, and save video timestamp when quitting
keep-open
save-position-on-quit

#default size of the window when launched, and a few other display-based options
geometry=50%x50%
no-taskbar-progress
no-border
cursor-autohide=100
osd-bar=no

#configuring the screenshot format, directory, and naming scheme
screenshot-format=png
screenshot-directory="~~/../Screenshots"
screenshot-high-bit-depth
screenshot-template="SCREENSHOT_%f-%wH.%wM.%wS.%wT"

#setting subtitle and audio track preference as per language (anime specific for me)
sub-auto=fuzzy
alang=jpn,ja,jp,en,eng
slang=enm,en,eng,jp,jpn,ja

#High quality video rendering for fast computer, you can try using this on high end PCs to use GPU
#for rendering video files, go through other configs for detailed info on this one, there are many
#options according to your graphics card
#profile=gpu-hq
#vo=gpu
#priority=high
#gpu-api=vulkan
#fbo-format=rgba16hf
#video-sync=display-resample

#I use these shaders instead of the heavy ones, because honestly, there’s no difference in quality if
#you’re using 1080p files (which is mostly what I watch), and they’re very lightweight.
scale=bilinear
cscale=bilinear
dscale=bilinear
scale-antiring=0
cscale-antiring=0
dither-depth=no
correct-downscaling=no
sigmoid-upscaling=no
deband=no
hwaccel=auto
hwdec=auto

##These are the heavy shaders I was talking about. You can tinker with them and try if you like it, but it’s not necessary. It’s more like a cherry on the top.
#gpu-shader-cache-dir="~~/shaders/cache"
#Shader bindings have been set in input.conf
{{< / highlight >}}
Make sure to create a folder named "Screenshots" (to save the screenshots) in the mpv-root folder if you’re using my config.

Links to some other good configs:

1.  [https://github.com/DeadNews/mpv-config/blob/main/mpv.conf](https://github.com/DeadNews/mpv-config/blob/main/mpv.conf)
2.  [https://github.com/LightArrowsEXE/dotfiles/blob/master/mpv/.config/mpv/mpv.conf](https://github.com/LightArrowsEXE/dotfiles/blob/master/mpv/.config/mpv/mpv.conf)

## Extending functionality with scripts
You can extend the functionality of mpv with scripts that are written in `.lua`.

To use a script, there might be some specific instructions on the developer’s page. But if it’s not mentioned, get the `.lua` file and place it in the `mpv-root >> portable_config >> scripts` directory and reopen your mpv.

I’ll share the two scripts I use myself and what they do. A comprehensive list can be found easily by googling  "mpv player scripts" and going to the GitHub pages.

1. [Autoload.lua](https://github.com/mpv-player/mpv/blob/master/TOOLS/lua/autoload.lua) – It loads all the files in your current playing video directory into mpv like a playlist.
2. [History-bookmark.lua](https://github.com/yuukidach/mpv-scripts/blob/master/history-bookmark.lua) - This script helps you to create a history file `.mpv.history` in the video folder. The next time you want to continue to watch it, you can open any videos in the folder. The script will lead you to the video played last time. It is like the **continue-watching** feature. Take a look at the mpv-scripts [GitHub repo](https://github.com/yuukidach/mpv-scripts) for details.

## Updating mpv
To update your mpv player, run the file `mpv-root >> updater.bat` with administrative privileges. It’ll fetch the latest package from github and update it.

## Other guides:
- [https://kokomins.wordpress.com/2019/10/14/mpv-config-guide/](https://kokomins.wordpress.com/2019/10/14/mpv-config-guide/)
- [https://iamscum.wordpress.com/guides/videoplayback-guide/](https://iamscum.wordpress.com/guides/videoplayback-guide/)

## Handy Resources
1.  MPV keybindings image path: `mpv-root/doc/mpbindings.png`
2.  MPV manual: `mpv-root/doc/manual.pdf`
3.  Online version of manual: [https://mpv.io/manual/stable/](https://mpv.io/manual/stable/)