# tip

> Connect to remote systems over a serial link.
> See also: `cu`, `minicom`, `picocom`, `tio`.
> More information: <https://manned.org/tip>.

- Connect to a serial device:

`sudo tip {{/dev/ttyXYZ}}`

- Connect to a serial device with a specific baud rate:

`sudo tip -{{baud_rate}} {{/dev/ttyXYZ}}`

- Connect to a system defined in `/etc/remote`:

`tip {{system_name}}`

- Connect in verbose mode:

`sudo tip -v -{{baud_rate}} {{/dev/ttyXYZ}}`

- Connect without interpreting `~` as an escape character:

`sudo tip -n -{{baud_rate}} {{/dev/ttyXYZ}}`

- Drop the connection and exit:

`<Enter><~><.>`
