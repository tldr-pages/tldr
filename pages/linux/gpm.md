# gpm

> Enable mouse support for the Linux virtual console.
> More information: <https://manned.org/gpm>.

- Start gpm with a PS/2 [m]ouse of [t]ype ps2:

`sudo gpm -m /dev/input/mice -t ps2`

- Start gpm with a Microsoft serial [m]ouse of [t]ype ms:

`sudo gpm -m /dev/ttyS0 -t ms`

- Start gpm in the foreground for [D]ebugging:

`sudo gpm -m {{path/to/mouse_device}} -t {{mouse_type}} -D`

- [k]ill the running gpm:

`sudo gpm -k`

- Start gpm in [R]epeater mode for X server compatibility:

`sudo gpm -m {{path/to/mouse_device}} -t {{mouse_type}} -R`

- List the available mouse [t]ypes:

`gpm -t help`
