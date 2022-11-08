# stty

> Set options for a terminal device interface.
> More information: <https://www.gnu.org/software/coreutils/stty>.

- Display all settings for the current terminal:

`stty --all`

- Set the number of rows:

`stty rows {{rows}}`

- Set the number of columns:

`stty cols {{cols}}`

- Get the actual transfer speed of a device:

`stty --file {{path/to/device_file}} speed`

- Reset all modes to reasonable values for the current terminal:

`stty sane`
