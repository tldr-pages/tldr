# minicom

> A program to do a serial communication with a device.
> More information: <https://manned.org/minicom>.

- Open a given serial port:

`sudo minicom --device {{/dev/ttyUSB0}}`

- Open a given serial port with a given baudrate:

`sudo minicom --device {{/dev/ttyUSB0}} --baudrate 115200`

- Enter setup page before doing communication with a given serial port:

`sudo minicom --device {{/dev/ttyUSB0}} --setup`
