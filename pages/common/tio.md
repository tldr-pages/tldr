# tio

> Command to monitor and interact with serial ports.
> More information: <https://github.com/tio/tio>.

- Open a serial port with default settings:

`tio {{/dev/ttyUSB0}}`

- Open a serial port with a specific baud rate:

`tio {{[-b|--baudrate]}} {{9600}} {{/dev/ttyUSB0}}`

- Open a serial port and log output to a file:

`tio -l {{log_file}} {{/dev/ttyUSB0}}`

- Open a serial port and enable hexadecimal output:

`tio -H {{/dev/ttyUSB0}}`

- List available serial ports:

`tio --list`
