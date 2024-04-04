# ydotool

> Control keyboard and mouse inputs via commands in a way that is display server agnostic.
> More information: <https://github.com/ReimuNotMoe/ydotool>.

- Start the ydotool daemon in the background:

`ydotoold`

- Perform a left click input:

`ydotool click 0xC0`

- Perform a right click input:

`ydotool click 0xC1`

- Input Alt+F4:

`ydotool key 56:1 62:1 62:0 56:0`
