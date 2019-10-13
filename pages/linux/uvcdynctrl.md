# uvcdynctrl

> A libwebcam command line tool to manage dynamic controls in uvcvideo.

- List all available cameras:

`uvcdynctrl -l`

- Specify the device to use (default='video0'):

`uvcdynctrl -d {{device_name}}`

- List available controls:

`uvcdynctrl -c`

- Set a new control value (For negative values: -s 'My Control' -- -42):

`uvcdynctrl -s {{control_name}} {{value}}`

- Retrieve  the  current  control  value:

`uvcdynctrl -g {{control_name}}`

- Save current controls state to a file:

`uvcdynctrl -W {{file_name}}`

- Load controls state from a file:

`uvcdynctrl -L {{file_name}}`
