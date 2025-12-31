# picocom

> Minimal program to emulate serial consoles.
> More information: <https://manned.org/picocom>.

- Connect to a serial console with the default baud rate of 9600:

`sudo picocom {{/dev/ttyXYZ}}`

- Connect to a serial console with a specified baud rate:

`sudo picocom {{/dev/ttyXYZ}} {{[-b|--baud]}} {{baud_rate}}`

- Map special characters (e.g. `LF` to `CRLF`):

`sudo picocom {{/dev/ttyXYZ}} --imap {{lfcrlf}}`

- Exit picocom:

`<Ctrl a><Ctrl x>`

- Display help:

`picocom {{[-h|--help]}}`
