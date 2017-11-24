# xdotool

> Command line automation for X11.

- Retrieve the X-Windows window ID of the running Firefox window(s):

`xdotool search --onlyvisible --name {{firefox}}`

- Click the right mouse button:

`xdotool click {{3}}`

- Get the id of the currently active window:

`xdotool getactivewindow`

- Focus on window with the id of 12345:

`xdotool windowfocus --sync 12345`

- Send a Hello World message with 500ms delay for each letter:

`xdotool type --delay 500 "Hello World"`

- Press enter:

`xdotool key KP_Enter`
