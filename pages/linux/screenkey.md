# screenkey

> A screencast tool to display your keys.
> More information: <https://www.thregr.org/~wavexx/software/screenkey/>.

- Display your keys pressed on the screen:

`screenkey`

- Display your keys and mouse buttons pressed on the screen:

`screenkey --mouse`

- Launch settings menu of screenkey:

`screenkey --show-settings`

- Change the postion(top/center/bottom/fixed) of screenkey:

`screenkey --position top`

- Change the modifiers displayed on the screen like ctrl to ⌘ in mac mode:

`screenkey --mods-mode mac`

- Change the appearance of screenkey:

`screenkey --bg-color '#353535' --font Hack --font-color yellow --opacity 0.8`

- Drag and select a window on screen to display screenkey:

`screenkey --position fixed --geometry $(slop -n -f '%g')`
