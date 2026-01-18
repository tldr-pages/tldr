# tio

> Monitor and interact with serial ports.
> More information: <https://github.com/tio/tio#3-usage>.

- Open a serial port with default settings:

`tio {{/dev/ttyUSB0}}`

- Open a serial port with a specific baud rate:

`tio {{[-b|--baudrate]}} {{9600}} {{/dev/ttyUSB0}}`

- Open a serial port and log output to a file:

`tio {{[-L|--log]}} --log-file {{log_file}} {{/dev/ttyUSB0}}`

- Open a serial port and enable hexadecimal output:

`tio --output-mode hex {{/dev/ttyUSB0}}`

- List available serial ports:

`tio {{[-l|--list]}}`
