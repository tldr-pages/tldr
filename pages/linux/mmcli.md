# mmcli

> Control and monitor the ModemManager.
> More information: <https://www.freedesktop.org/software/ModemManager/man/latest/mmcli.1.html>.

- List available modems:

`mmcli --list-modems`

- Print information about a modem:

`mmcli --modem={{modem}}`

- Enable a modem:

`mmcli --modem={{modem}} --enable`

- List SMS messages available on the modem:

`sudo mmcli --modem={{modem}} --messaging-list-sms`

- Delete a message from the modem, specifying its path:

`sudo mmcli --modem={{modem}} --messaging-delete-sms={{path/to/message_file}}`
