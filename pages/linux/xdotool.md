# xdotool

> Automate X11 actions.
> More information: <https://manned.org/xdotool>.

- Retrieve the X-Windows window ID of the running Firefox window(s):

`xdotool search --onlyvisible --name firefox`

- Perform a mouse `<RightClick>`:

`xdotool click 3`

- Get the ID of the currently active window:

`xdotool getactivewindow`

- Focus on the window with a specific ID:

`xdotool windowfocus --sync {{12345}}`

- Type a message, with a 500ms delay for each letter:

`xdotool type --delay 500 "{{Hello world}}"`

- Press the `<Enter>` key:

`xdotool key KP_Enter`
