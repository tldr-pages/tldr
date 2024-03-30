# uvcdynctrl

> A libwebcam command-line tool to manage dynamic controls in uvcvideo.
> More information: <https://manned.org/uvcdynctrl>.

- List all available cameras:

`uvcdynctrl -l`

- Use a specific device (defaults to `video0`):

`uvcdynctrl -d {{device_name}}`

- List available controls:

`uvcdynctrl -c`

- Set a new control value (for negative values, use `-- -value`):

`uvcdynctrl -s {{control_name}} {{value}}`

- Get the current control value:

`uvcdynctrl -g {{control_name}}`

- Save the state of the current controls to a file:

`uvcdynctrl -W {{filename}}`

- Load the state of the controls from a file:

`uvcdynctrl -L {{filename}}`
