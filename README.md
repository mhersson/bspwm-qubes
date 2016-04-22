# bspwm-qubes
Misc stuff for running bspwm on qubes-os

## change_focused_border_color.py
Listens for property change events to see if the active/focused window has shifted. 
Then reads the _QUBES_LABEL property and sets the focused border color accordingly.
Depends on [xpybutil] (https://github.com/BurntSushi/xpybutil.git). 
Install by transfering xpybutil to dom0 and run *sudo setup.py install* from within the xpybutil repos directory. 
You can start change_focused_border_color.py from within bspwmrc.

## download_and_build
Contains a download and build script and spec files for bspwm, sxhkd, lemonbar, sutil, xtitle 
