# setserial

> Read and modify serial port information.
> More information: <https://manned.org/setserial>.

- Print all information of a serial device:

`setserial -a {{/dev/cua0}}`

- Print the configuration summary of a specific serial device (useful for printing during bootup process):

`setserial -b {{device}}`

- Set a specific configuration parameter to a device:

`sudo setserial {{device}} {{parameter}}`

- Print the configuration of a list of devices:

`setserial -g {{device1 device2 ...}}`
