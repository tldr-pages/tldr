# minicom

> Communicate with the serial interface of a device.
> More information: <https://manned.org/minicom>.

- Open a given serial port:

`sudo minicom {{[-D|--device]}} {{/dev/ttyXYZ}}`

- Open a given serial port with a given baud rate:

`sudo minicom {{[-D|--device]}} {{/dev/ttyXYZ}} {{[-b|--baudrate]}} {{115200}}`

- Enter the configuration menu before communicating with a given serial port:

`sudo minicom {{[-D|--device]}} {{/dev/ttyXYZ}} {{[-s|--setup]}}`

- Capture the output of a serial port to a file:

`sudo minicom {{[-D|--device]}} {{/dev/ttyXYZ}} {{[-C|--capturefile]}} {{path/to/file}}`

- Exit minicom:

`<Ctrl a><x><Enter>`

- Display help:

`minicom {{[-h|--help]}}`
