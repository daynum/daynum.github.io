+++
title = 'Setting Up Centos for Development'
date = 2023-12-21T06:25:05+05:30
draft = true
+++

{{<table_of_contents>}}

## Table Of Contents

This is a guide I made for myself.
These are all the steps I do, when I have a fresh centOS VM and I need to make it development ready. To start coding.

First, Get a clean VM with a base image as CentOS.

Update the VM
```bash
sudo yum update
```

Ensure `git` is installed
```bash
sudo yum install git -y
```

---
### Setup ZSH and omz

I like to change my default shell from bash to [ZSH](https://www.zsh.org/), and install [OhMyZSH](https://ohmyz.sh/) on top of it. [OMZ Github](https://github.com/ohmyzsh/ohmyzsh). It looks very good, and gives useful extensions which makes life easier.
Like [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions) and [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)

[Install ZSH](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH) - You can take a look at this guide from OMZ github to install ZSH.

In short, Install ZSH on the centOS VM with:
```bash
sudo yum install zsh -y
```

Check these outputs, we are checking here that what path is returned when we invoke zsh from user mode and root mode, just for info.
```bash
# this should output '/usr/bin/zsh'
which zsh 

# this should output '/bin/zsh'
sudo which zsh
```

Verify with this command that zsh is added to `/etc/shells`(it's a file which maintains a list of available shells), without it we won't be able to properly switch to zsh.
```bash
# Add entry of zsh to /etc/shells if not present
command -v zsh | sudo tee -a /etc/shells
```

Change the user shell to point to zsh (output from previous commands is used here).
I'm not sure if we should change the shell for the root as well, it might be a bad thing to do. But I did it anyway to see if anything bad happens, just to tinker.
```bash
#change the user shell
chsh -s /usr/bin/zsh

# change the root shell
sudo chsh -s /bin/zsh
```

Quit your shell and login again

Add oh-my-zsh to your zsh.
```bash
# download and install omz
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

```

Add these 2 useful plugins to your zsh terminal, for autocompletion and syntax-highlighting of commands as you type.

First clone the repositories for the plugins.
```bash
# download autocomplete plugin 
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions

# download syntax highlighter plugin
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting

```

Now we need to add these plugins to out `.zshrc` file (this is the configuration file for your zsh installation).
Here, find the line which says `plugins=(git)` and add the plugins to it, like below.
```bash
# edit zshrc
vi ~/.zshrc

# find this > plugins=(git)
# add zsh-autosuggestions & zsh-syntax-highlighting to this list
# looks like this then
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

# Reload your terminal config
source ~/.zshrc
```

--- 

### Install Python and VirtualEnv
Now I need python to work on codebase, and i need multiple versions of python too, so I use pyenv to manage my python versions.
And pyenv-virtualenv to manage my virtual environments. It makes managing different python versions very easy.
Install pyenv and pyenv-virtualenv
```bash
# download pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# Add pyenv root to zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc

# Add path manipulator to zshrc (need this for pyenv to work)
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc

# Add directory evaluator to zshrc, need this for changing virtualenv when moving between directories
# This is optioonal, if you like to activate and deactivate your venv by entering commands, you can skip this.
# This command will automatically activate and deactivate, the virtual environment OR local python version - if you've set specific python version for a directory,
# when you change directory in and out of a directory which has virtual environment file initialized (child subdirectories maintain the activated venv)
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc

# Restart your shell with
exec "$SHELL"

# Install pyenv-virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

# Add config to zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# Restart your shell with
exec "$SHELL"

# List current python versions in pyenv with
pyenv versions
```
Follow up with [pyenv documentation](https://github.com/pyenv/pyenv) if you want to learn more about all the available commands.

Install developer packages before installing any python version, these are needed while building and installing python
```bash
sudo yum install postgresql-devel
sudo yum install python-devel
sudo yum install python3-devel
sudo yum install unixODBC-devel
sudo yum install gcc openssl-devel bzip2-devel sqlite-devel

```

Just going little bit off track here, if you have UBUNTU instead os centOS, below are the development dependencies you need to install.
```bash
sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
sudo apt install liblzma-dev libsqlite3-dev 
sudo apt-get install build-essential zlib1g-dev libffi-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev liblzma-dev
```

Now install the python version you want with pyenv, here are a bunch of commonly used commands.
```bash
# Install python3.6 with
pyenv install 3.6.15

# Create a global virtual environment to be used (to not mess anything up with existing system python)
pyenv virtualenv 3.6.15 global_venv_3.6.15

# Set the above virtual environment as global, just python version can be set as global too.
pyenv global global_venv_3.6.15

# Now you'll be working under this virtual environment by default
```

---

### Install Java and maven

Ensure JAVA 1.8, or whatever version your project needs.
```bash
sudo yum install java-1.8.0-openjdk -y
```

Ensure maven
```bash
sudo yum install maven -y
```

Now this maven version might not work for you sometimes I've seen it, most likely it won't as of now.
To fix it we need to replace our maven files with the latest maven release, centOS's package manager yum doesn't install the latest one.

```bash
# Run this just to check version, and the path where current maven is installed
mvn -version
# In the output my maven home was: /usr/share/maven
# So we need to download the latest maven and replace this old one with the new one.
```

Download latest maven from apache. You can skip the below command block and just go to https://maven.apache.org/download.cgi and get the latest maven version.
the filename should end in .tar.gz though. Also we need to keep the download location (path) handy. Here my download path is `/tmp`.

```bash
# Go to https://maven.apache.org/download.cgi and look what the latest maven is
# We need the .tar.gz versions for our centOS, at this time the version is 3.9.0
# The file name i can see on the apache website is apache-maven-3.9.0-bin.tar.gz right click and copy the link to this
# Download the maven file with [ wget <link-you-copied> -P /tmp]
wget https://dlcdn.apache.org/maven/maven-3/3.9.0/binaries/apache-maven-3.9.0-bin.tar.gz -P /tmp

# Keep the filename handy we'll need it
```

Rename the old maven folder to something else as backup, so we can use it if things break.
```bash
sudo mv /usr/share/maven /usr/share/maven_bkp
```

extract the maven .tar.gz file, replace `/tmp` with your download path.
```bash
# Extract with sudo tar xf /<your-download-path>/<your-file-name> -C /usr/share
sudo tar xf /tmp/apache-maven-3.9.0-bin.tar.gz -C /usr/share
```

Rename the extracted maven folder to standard maven direeory name.
```bash
# Newly extracted maven folder will have its name as <your-file-name> minus the '-bin.tar.gz' part
# Change this to the generic name used by system
sudo mv /usr/share/apache-maven-3.9.0 /usr/share/maven
```

Remove the tar file if you want
```bash
# rm /tmp/<your-file-name>
rm /tmp/apache-maven-3.9.0-bin.tar.gz
```

Verify with maven version
```bash
# Run this to verify that the current maven version is what we just installed
mvn -version
```

--- 

### Installing npm and node.

Install nvm, check the nvm-sh github repo for the latest download version, I have the version `0.39.3` here.
```bash
# Download and install nvm to manage node and npm, this same command is used to update the nvm.
# Check 
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

# To reload the bash (same as quit and reopen)
exec "$SHELL"
```

Install node version you need, I am installing `8.16.1` here.
```bash
# Install node version 8.16.1
nvm install 8.16.1
nvm use 8.16.1
```

Enable EPEL (Extra Packages for Enterprise Linux) respository in centOS, to install other required packages you will definitely need.
```bash
# This command is centOS 7 specific, i referred this webpage: https://www.tecmint.com/install-epel-repo-rhel-rocky-almalinux/
sudo yum install epel-release -y
```
