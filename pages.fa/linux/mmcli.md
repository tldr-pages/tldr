# mmcli

> کنترل و پایش ModemManager.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/ModemManager/man/latest/mmcli.1.html>.

- فهرست کردن مودم‌های موجود:

`mmcli {{[-L|--list-modems]}}`

- فهرست کردن مودم‌های موجود و پایش مودم‌های افزوده یا حذف‌شده:

`mmcli {{[-M|--monitor-modems]}}`

- چاپ اطلاعات مودم:

`mmcli {{[-m|--modem]}} {{modem_number}}`

- فعال کردن مودم:

`mmcli {{[-m|--modem]}} {{modem_number}} {{[-e|--enable]}}`

- فهرست کردن پیام‌های SMS موجود در مودم:

`sudo mmcli {{[-m|--modem]}} {{modem_number}} --messaging-list-sms`

- حذف پیام از مودم با تعیین مسیر آن:

`sudo mmcli {{[-m|--modem]}} {{modem_number}} --messaging-delete-sms {{path/to/message_file}}`
