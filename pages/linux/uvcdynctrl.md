# uvcdynctrl

> Manage dynamic controls in uvcvideo.
> More information: <https://manned.org/uvcdynctrl>.

- List all available cameras:

`uvcdynctrl {{[-l|--list]}}`

- Use a specific device (defaults to `video0`):

`uvcdynctrl {{[-d|--device]}} {{device_name}}`

- List available controls:

`uvcdynctrl {{[-c|--clist]}}`

- Set a new control value (for negative values, use `-- -value`):

`uvcdynctrl {{[-s|--set]}} {{control_name}} {{value}}`

- Get the current control value:

`uvcdynctrl {{[-g|--get]}} {{control_name}}`

- Save the state of the current controls to a file:

`uvcdynctrl {{[-W|--save]}} {{filename}}`

- Load the state of the controls from a file:

`uvcdynctrl {{[-L|--load]}} {{filename}}`
