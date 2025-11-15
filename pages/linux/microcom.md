# microcom

> A minimalistic terminal program, used to access remote devices via a serial, CAN or telnet connection from the console.
> More information: <https://manned.org/microcom>.

- Open a serial port using the specified baud rate:

`microcom {{[-p|--port]}} {{/dev/ttyXYZ}} {{[-s|--speed]}} {{baud_rate}}`

- Establish a telnet connection to the specified host:

`microcom {{[-t|--telnet]}} {{hostname}}:{{port}}`
