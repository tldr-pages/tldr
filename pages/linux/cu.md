# cu

> Call Up another system and act as a dial-in/serial terminal or perform file transfers with no error checking.
> More information: <https://manned.org/cu>.

- Open a given serial port:

`sudo cu {{[-l|--line]}} {{/dev/ttyXYZ}}`

- Open a given serial port with a given baud rate:

`sudo cu {{[-l|--line]}} {{/dev/ttyXYZ}} {{[-s|--speed]}} {{115200}}`

- Open a given serial port with a given baud rate and echo characters locally (half-duplex mode):

`sudo cu {{[-l|--line]}} {{/dev/ttyXYZ}} {{[-s|--speed]}} {{115200}} {{[-h|--halfduplex]}}`

- Open a given serial port with a given baud rate, parity, and no hardware or software flow control:

`sudo cu {{[-l|--line]}} {{/dev/ttyXYZ}} {{[-s|--speed]}} {{115200}} --parity={{even|odd|none}} {{[-f|--nortscts]}} --nostop`

- Exit the `cu` session when in connection:

`<Enter><~><.>`

- Display help:

`cu --help`
