---
title: Using Pacman
date: 10/12/2023
---

#### Querying / searching package database
Search for a string in package name and package description
`pacman -Ss string1 string2 ...`

Search in already installed packages
`pacman -Qs string1 string2 ...`

Display extensive information about a given package
`pacman -Si <package_name>`

Display extensive information about local package
`pacman -Qi <package_name>`

List all packages no longer required as dependencies (orphans):
`pacman -Qdt`

List all packages explicitly installed and not required as dependencies:
`pacman -Qet`

---
#### Install packages

`pacman -S <package-name1> <package-name2> ...`

---
#### Upgrading packages
Upgrade all packages, full-system upgrade
`pacman -Syu`

---
#### Removing Packages

Remove a single package without removing it's dependencies
`pacman -R <package_name>`

Remove a package and its dependencies which are not required by any other installed package
`pacman -Rs <package_name>`

Remove a package, its dependencies and all the packages that depend on the target package. Care needed, can potentially remove everything.
`pacman -Rsc <package_name>`

Remove a package, which is required by another package, without removing the dependent package
`pacman -Rdd <package_name>`

Remove not needed packages, by chaining commands
`pacman -Rns $(pacman -Qdtq)`

Pacman's created extra config files and backups for the system can be removed with 
`pacman -Rn`

---
#### Cache cleaning

Remove all the cached packages that are not currently installed, and the unused sync databases, execute:
`pacman -Sc`

Remove all files from the cache, use the clean switch twice, this is the most aggressive approach and will leave nothing in the cache directory:
`pacman -Scc`

---
#### Flags
`-S, --sync` : Syncs the package repositories.
