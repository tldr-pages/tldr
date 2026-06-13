# setserial

> Read and modify serial port information.
> More information: <https://manned.org/setserial>.

- Print all information about a specific serial device:

`setserial -a {{/dev/cuaN}}`

- Print the configuration summary of a specific serial device (useful for printing during bootup process):

`setserial -b {{device}}`

- Set a specific configuration parameter to a device:

`sudo setserial {{device}} {{parameter}}`

- Print the configuration of a list of devices:

`setserial -g {{device1 device2 ...}}`
