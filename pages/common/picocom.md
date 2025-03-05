# picocom

> Minimal program to emulate serial consoles.
> More information: <https://manned.org/picocom>.

- Connect to a serial console and negotiate baud rate:

`sudo picocom {{/dev/ttyXYZ}}`

- Connect to a serial console with a specified baud rate:

`sudo picocom {{/dev/ttyXYZ}} --baud {{baud_rate}}`

- Map special characters (e.g. `LF` to `CRLF`):

`sudo picocom {{/dev/ttyXYZ}} --imap {{lfcrlf}}`
