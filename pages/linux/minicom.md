# minicom

> Communicate with the serial interface of a device.
> More information: <https://manned.org/minicom>.

- Open a given serial port:

`sudo minicom --device {{/dev/ttyUSB0}}`

- Open a given serial port with a given baud rate:

`sudo minicom --device {{/dev/ttyUSB0}} --baudrate {{115200}}`

- Enter the configuration menu before communicating with a given serial port:

`sudo minicom --device {{/dev/ttyUSB0}} --setup`
