# mmcli

> Controlați și monitorizați ModemManager.
> Mai multe informaţii: <https://www.freedesktop.org/software/ModemManager/man/latest/mmcli.1.html>

- Lista mesajelor SMS disponibile pe modem:

`sudo mmcli --modem={{modem}} --messaging-list-sms`

- Ștergeți un mesaj din modem, specificând calea sa:

`sudo mmcli --modem={{modem}} --messaging-delete-sms={{path/to/message_file}}`
