# mmcli

> Control and monitor the ModemManager.
> More information: <https://www.freedesktop.org/software/ModemManager/man/1.0.0/mmcli.8.html>.

- List SMS messages available on the modem:

`sudo mmcli -m {{modem}} --messaging-list-sms`

- Delete a message from the modem by path:

`sudo mmcli -m {{modem}} --messaging-delete-sms={{path}}`
