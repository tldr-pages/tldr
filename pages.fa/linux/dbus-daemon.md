# dbus-daemon

> سرویس پیام D-Bus که به چند برنامه اجازهٔ تبادل پیام می‌دهد.
> اطلاعات بیشتر: <https://dbus.freedesktop.org/doc/dbus-daemon.1.html>.

- اجرای سرویس با یک فایل پیکربندی:

`dbus-daemon --config-file {{path/to/file}}`

- اجرای سرویس با پیکربندی استاندارد گذرگاه پیام ویژهٔ هر نشست ورود:

`dbus-daemon --session`

- اجرای سرویس با پیکربندی استاندارد گذرگاه پیام سراسری سیستم:

`dbus-daemon --system`

- تنظیم آدرس گوش دادن و جایگزینی مقدار پیکربندی آن:

`dbus-daemon --address {{address}}`

- چاپ شناسهٔ فرایند در خروجی استاندارد `stdout`:

`dbus-daemon --print-pid`

- وادار کردن گذرگاه پیام به نوشتن پیام‌ها در گزارش سیستم:

`dbus-daemon --syslog`
