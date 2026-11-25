# systemd-stdio-bridge

> پیاده‌سازی پراکسی بین `stdin`/`stdout` و D-Bus.
> توجه: هنگام شروع انتظار اتصال باز از طریق `stdin`/`stdout` دارد و اتصال جدیدی به گذرگاه مشخص ایجاد می‌کند.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-stdio-bridge.html>.

- هدایت `stdin`/`stdout` به گذرگاه سیستم محلی:

`systemd-stdio-bridge`

- هدایت `stdin`/`stdout` به D-Bus کاربر مشخص:

`systemd-stdio-bridge --{{user}}`

- هدایت `stdin`/`stdout` به گذرگاه سیستم محلی در کانتینر مشخص:

`systemd-stdio-bridge {{[-M|--machine]}} {{mycontainer}}`

- هدایت `stdin`/`stdout` به آدرس D-Bus دلخواه:

`systemd-stdio-bridge {{[-p|--bus-path]}} unix:path=/{{path/to/dbus_socket}}`
