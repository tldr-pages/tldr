# minicom

> Communicate with the serial interface of a device.
> More information: <https://manned.org/minicom>.

- Open a given serial port:

`sudo minicom --device {{/dev/ttyXYZ}}`

- Open a given serial port with a given baud rate:

`sudo minicom --device {{/dev/ttyXYZ}} --baudrate {{115200}}`

- Enter the configuration menu before communicating with a given serial port:

`sudo minicom --device {{/dev/ttyXYZ}} --setup`

- Exit minicom:

`<Ctrl a><x><Enter>`
