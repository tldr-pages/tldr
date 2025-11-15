# stty

> Set options for a terminal device interface.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

- Display current terminal size:

`stty size`

- Display all settings for the current terminal:

`stty {{[-a|--all]}}`

- Set the number of rows or columns:

`stty {{rows|cols}} {{count}}`

- Get the actual transfer speed of a device:

`stty {{[-F|--file]}} {{path/to/device_file}} speed`

- Reset all modes to reasonable values for the current terminal:

`stty sane`

- Switch between raw and normal mode:

`stty {{raw|cooked}}`

- Turn character echoing off or on:

`stty {{-echo|echo}}`

- Display help:

`stty --help`
