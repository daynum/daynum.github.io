---
title: Using Git Worktrees
date: 30/11/2025
---
Git worktrees can keep track of your changes on different branches, with no need to stash or commit. 
It basically is same as the manual way - creating multiple folders for different branches and making changes there independently.
Git worktrees do the same thing but with git native and lightweight way.

How to use:
My personal way of structuring is:
```bash
projects
|- repo1 (no clone here, just to keep it tidy)
|    |
|    |-- repo1-master (clone here)
|    |-- repo1-feature1 (this created by git worktree)
|- repo2
     |-- repo2-master
```

```bash
mkdir <your-repo-name> && cd <your-repo-name>
git clone <your-repo-name>

# list current worktrees
git worktree list

# Now 3 cases for creating worktrees

# If the branch is already available locally (fetched from github, local git knows about branch)
# This creates a worktree in the directory ../feature-a and checks it out
git worktree add ../feature-a feature-a

# If the branch does not exist locally yet, but is available on github.
# You tell git to base the new local branch on the github branch by giving name to it.
git worktree add -b feature-b ../feature-b origin/feature-b

# If the branch you want to work on is completely new and not even created on GitHub.
# Then you need to tell, on where to "base" this branch on and create it locally.
# Notice that in above scenario also we have a "base" for our new local branch, jsut the base is remote there and base is master branch here.
git worktree add -b feature-c ../feature-c master
```