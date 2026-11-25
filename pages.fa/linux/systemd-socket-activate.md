# systemd-socket-activate

> فعال‌سازی سوکت برای سرویس‌های systemd.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-socket-activate.html>.

- فعال کردن سرویس هنگام اتصال سوکت مشخص:

`systemd-socket-activate {{path/to/socket.service}}`

- فعال کردن چند سوکت برای سرویس:

`systemd-socket-activate {{path/to/socket1.service}} {{path/to/socket2.service}}`

- ارسال متغیرهای محیطی به سرویس در حال فعال‌سازی:

`{{SYSTEMD_SOCKET_ACTIVATION=1}} systemd-socket-activate {{path/to/socket.service}}`

- فعال کردن سرویس همراه با سوکت اعلان:

`systemd-socket-activate {{path/to/socket.socket}} {{path/to/service.service}}`

- فعال کردن سرویس با پورت مشخص:

`systemd-socket-activate {{path/to/socket.service}} {{[-l|--listen]}} {{8080}}`
