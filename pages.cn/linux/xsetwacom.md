# xsetwacom

> Command line tool to change settings for Wacom pen tablets at runtime.

- List all the available wacom devices. The device name is in the first column:

`xsetwacom list`

- Set Wacom area to specific screen. Get name of the screen with `xrandr`:

`xsetwacom set "{{device_name}}" MapToOutput {{screen}}`

- Set mode to relative (like a mouse) or absolute (like a pen) mode:

`xsetwacom set "{{device_name}}" Mode "{{Relative|Absolute}}"`

- Rotate the input (useful for tablet-PC when rotating screen) by 0|90|180|270 degrees from "natural" rotation:

`xsetwacom set "{{device_name}}" Rotate {{none|half|cw|ccw}}`

- Set button to only work when the tip of the pen is touching the tablet:

`xsetwacom set "{{device_name}}" TabletPCButton "on"`
