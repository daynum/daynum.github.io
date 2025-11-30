---
title: Using screen in Linux
date: 30/11/2024
---

Get list of commands, when inside a screen
```bash
Ctrl+a ?
```

New screen session
```bash
screen -S session_name
```

Common commands
- `Ctrl+a` `c` Create a new window (with shell).
- `Ctrl+a` `"` List all windows.
- `Ctrl+a` `0` Switch to window 0 (by number).
- `Ctrl+a` `A` Rename the current window.
- `Ctrl+a` `S` Split current region horizontally into two regions.
- `Ctrl+a` `|` Split current region vertically into two regions.
- `Ctrl+a` `tab` Switch the input focus to the next region.
- `Ctrl+a` `Ctrl+a` Toggle between the current and previous windows
- `Ctrl+a` `Q` Close all regions but the current one.
- `Ctrl+a` `X` Close the current region.
- `Ctrl+a` `d` Detach from screen
- `screen -r` Reattach to screen
- `screen -ls` List screens

