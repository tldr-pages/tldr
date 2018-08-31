# stty

> Set options for a terminal device interface.

- Display all settings for the current terminal:

`stty -a`

- Set the number of rows:

`stty rows {{rows}}`

- Set the number of columns:

`stty cols {{cols}}`

- Get the only actual transfer speed of a device:

`stty -f /dev/stdout speed`

- Reset all modes to reasonable values for the current terminal:

`stty sane`
