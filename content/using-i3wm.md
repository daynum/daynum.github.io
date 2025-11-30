---
title: Using i3wm
date: 24/11/2023
---
Mod key is Windows Key.

- `Mod+Enter` -> Open Terminal
- `Mod+d`-> Open dmenu, search for any app.
- `Mod+shift+q`-> Close currently highlighted window.
- `Mod+arrow key`-> Switch to different window.
- `Mod+s`-> Organize windows as a stack.
- `Mod+w`-> Organize windows as tabs.
- `Mod+e`-> Back to tiled windows (default).
- `Mod+v`-> Switch the new window split to vertical.
- `Mod+h`-> Switch the new window split back to horizontal.
- `Mod+shift+arrow key`-> Move the window to desired tile/tab/stack position.
- `Mod+r`-> Enter resize mode. `Esc` to exit resize mode.
	- `Mod+right arrow`-> Increase window size horizontally.
	- `Mod+left arrow`-> Decrease window size horizontally.
	- `Mod+down arrow`-> Increase window size vertically.
	- `Mod+up arrow`-> Decrease window size vertically.
- `Mod+<number>`-> Move to the workspace "number".
- `Mod+shift+<number>`-> Move the focused window to workspace "number".
- `Mod+Shift+e`-> Exit i3 (similar to logout)
- `Mod+Enter` and then terminal command `i3lock` locks the i3, showing a blank screen, enter password to unlock.


- `Terminal: i3-config-wizard`-> If you forgot to create a config file in beginning.
- `~/.config/i3/config`-> i3 config file path.
- `Mod+shift+r`-> Restart i3 (kinda sourcing the new config)

##### Custom Key-Binding

You can change any of the existing keybindings in the i3 config file, all bindings (including all defaults) are written there. Be sure to not have duplicate keybindings, or your i3 will give config error.
[i3wm-documentation](https://www.i3wm.org/docs/)

```bash
# bindsym $<key-combo> exec <command>
# below line in config sets the keybinding mod+shift+x to lock the i3wm screen.
bindsym $mod+shift+x exec i3lock
```

Multimedia keybindings do not work by default on i3, because they are not set-up. This is a common problem, hence there is a [snippet](https://faq.i3wm.org/question/3747/enabling-multimedia-keys.1.html) already, you can add it to your i3 to enable multimedia keybindings.
```bash
# Pulse Audio controls
bindsym XF86AudioRaiseVolume exec --no-startup-id pactl set-sink-volume 0 +5% #increase sound volume
bindsym XF86AudioLowerVolume exec --no-startup-id pactl set-sink-volume 0 -5% #decrease sound volume
bindsym XF86AudioMute exec --no-startup-id pactl set-sink-mute 0 toggle # mute sound

# Sreen brightness controls
bindsym XF86MonBrightnessUp exec xbacklight -inc 20 # increase screen brightness
bindsym XF86MonBrightnessDown exec xbacklight -dec 20 # decrease screen brightness

# Touchpad controls
bindsym XF86TouchpadToggle exec /some/path/toggletouchpad.sh # toggle touchpad

# Media player controls
bindsym XF86AudioPlay exec playerctl play
bindsym XF86AudioPause exec playerctl pause
bindsym XF86AudioNext exec playerctl next
bindsym XF86AudioPrev exec playerctl previous
```

To put stuff on secondary monitor too
```bash
xrandr --auto
```
