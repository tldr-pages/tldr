# picocom

> Minimal program to emulate serial consoles.
> More information: <https://manned.org/picocom>.

- Connect to a serial console with a specified baud rate:

`picocom {{/dev/ttyXYZ}} --baud {{baud_rate}}`

- Map special characters (e.g. `LF` to `CRLF`):

`picocom {{/dev/ttyXYZ}} --imap {{lfcrlf}}`
