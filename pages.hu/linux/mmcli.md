# mmcli

> A ModemManager vezérlése és felügyelete. További információ: <https://www.freedesktop.org/software/ModemManager/man/latest/mmcli.1.html>.

- A modemen elérhető SMS-üzenetek listája:

`sudo mmcli --modem={{modem}} --messaging-list-sms`

- Üzenet törlése a modemről, megadva annak elérési útvonalát:

`sudo mmcli --modem={{modem}} --messaging-delete-sms={{path/to/message_file}}`
