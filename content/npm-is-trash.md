---
title: Npm Is Trash
date: 2024-04-15
---

Yesterday I installed NPM to install a package which can reload local server on file changes for my static website. I was using Arch on my machine, very happy.
Now, when i tried installing node pakages, it gave me the below error at first.

```bash
Error: EACCES: permission denied, mkdir '/usr/lib/node_modules/browser-sync'
```

I quickly google searched the error and found the [first result](https://stackoverflow.com/questions/39985691/permission-denied-when-installing-browsersync-via-npm) from stack over flow. Not wasting any time I went to the first answer and saw the command with `sudo chown` to change the permissions of required directory.  
At this point I thought `/usr` directory is meant for the user, little did I know this will lead to a disaster, and it actually means `unix system resources` historically.  
I went ahead and changed the permission of the directory which threw error, then changed permission for a few more directories, which gave me error. And it included the `/usr/bin` directory. Node got installed, happy. I set out to do my work.  
Then i ran pacman with sudo and it gave me error, then i tried a bunch of comamnds with sudo, all gave me the below error. My `sudo` is ruined!
```bash
sudo: /usr/bin/sudo must be owned by uid 0 and have the setuid bit set
```

I panicked and searched for a solution, and my heart sank as i saw answers telling a reinstall of OS. One way was to login as root, and change permission of `/usr/bin/sudo` again. I tried doing it, but `sudo su` did not work to become root, and I did not know how to login as root through sddm. There were some answers pointing to editing a file to enable logging in as root via sddm, but gues what? I would need sudo to edit them!  

In the end I gave up, and quickly reinstalled arch to restore the working of my machine, huge wastage of time. But I'll console myself by telling that i learned to not touch the permissions of `/usr` directory naively again :)  

What's worse is that NPM itself suggests this method of fixing the issue. How bad can they be? they're bloat, they're slow, they pollute with heavy packages, and now they're destroying PCs too! I hate NPM.  

