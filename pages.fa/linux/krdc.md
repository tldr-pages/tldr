# krdc

> اتصال به سرور دسکتاپ راه دور.
> اطلاعات بیشتر: <https://invent.kde.org/network/krdc#usage>.

- شروع KRDC:

`krdc`

- اتصال خودکار به میزبان با نام کاربری فعلی از طریق VNC:

`krdc {{remote_host}}`

- تعیین پروتکل و نام کاربری برای اتصال به میزبان:

`krdc {{vnc|rdp}}://{{username}}@{{remote_host}}`

- شروع اتصال در حالت تمام‌صفحه:

`krdc {{rdp://username@ip_address}} --fullscreen`
