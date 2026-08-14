# mmcli

> Control and monitor the ModemManager.
> More information: <https://www.freedesktop.org/software/ModemManager/man/latest/mmcli.1.html>.

- List available modems:

`mmcli {{[-L|--list-modems]}}`

- List available modems and monitor for ones added or removed:

`mmcli {{[-M|--monitor-modems]}}`

- Print information about a modem:

`mmcli {{[-m|--modem]}} {{modem_number}}`

- Enable a modem:

`mmcli {{[-m|--modem]}} {{modem_number}} {{[-e|--enable]}}`

- List SMS messages available on the modem:

`sudo mmcli {{[-m|--modem]}} {{modem_number}} --messaging-list-sms`

- Delete a message from the modem, specifying its path:

`sudo mmcli {{[-m|--modem]}} {{modem_number}} --messaging-delete-sms {{path/to/message_file}}`
