# cu

> Call Up another system and act as a dial-in/serial terminal or perform file transfers with no error checking.
> More information: <https://manned.org/cu>.

- Open a given serial port:

`sudo cu --line {{/dev/ttyUSB0}}`

- Open a given serial port with a given baud rate:

`sudo cu --line {{/dev/ttyUSB0}} --speed {{115200}}`

- Open a given serial port with a given baud rate and echo characters locally (half-duplex mode):

`sudo cu --line {{/dev/ttyUSB0}} --speed {{115200}} --halfduplex`

- Open a given serial port with a given baud rate, parity, and no hardware or software flow control:

`sudo cu --line {{/dev/ttyUSB0}} --speed {{115200}} --parity={{even|odd|none}} --nortscts --nostop`

- Exit the `cu` session when in connection:

`~.`
