# xdotool

> Command-line automation for X11.
> More information: <https://manned.org/xdotool>.

- Retrieve the X-Windows window ID of the running Firefox window(s):

`xdotool search --onlyvisible --name {{firefox}}`

- Click the right mouse button:

`xdotool click {{3}}`

- Get the ID of the currently active window:

`xdotool getactivewindow`

- Focus on the window with ID of 12345:

`xdotool windowfocus --sync {{12345}}`

- Type a message, with a 500ms delay for each letter:

`xdotool type --delay {{500}} "Hello world"`

- Press the enter key:

`xdotool key {{KP_Enter}}`
