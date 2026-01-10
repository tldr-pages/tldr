# gpm

> Enable mouse support for the Linux virtual console.
> More information: <https://manned.org/gpm>.

- Start gpm with a PS/2 mouse:

`sudo gpm -m /dev/input/mice -t ps2`

- Start gpm with a serial mouse on COM1:

`sudo gpm -m /dev/ttyS0 -t ms`

- Start gpm in the foreground for debugging:

`sudo gpm -m {{path/to/mouse_device}} -t {{mouse_type}} -D`

- Kill the running gpm:

`sudo gpm -k`

- Start gpm in repeater mode for X server compatibility:

`sudo gpm -m {{path/to/mouse_device}} -t {{mouse_type}} -R`

- List the available mouse types:

`gpm -t help`
