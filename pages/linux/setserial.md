# setserial

> Read or modify a LInux serial port information.
> More information: <https://linux.die.net/man/8/setserial>.

- Print all information of the supplied serial device (usually of the form /dev/cua[0-3]):

`setserial -a {{device}}`

- Print a summary of confguration of the serial device (useful for printing during bootup process):

`setserial -b {{device}}`

- Set configuration parameters to a device by passing commandline arguments. Superuser privilege is required in most cases:

`sudo setserial {{device}} {{parameter}}`

- Read configuration of a list of devices by using the `-g` option:

`setserial -g {{device1}} {{device2}} ...`
