# daemonize

> اجرای یک دستور که خود به سرویس تبدیل نمی‌شود، به‌صورت سرویس یونیکسی.
> اطلاعات بیشتر: <https://software.clapper.org/daemonize/>.

- اجرای یک دستور به‌صورت سرویس:

`daemonize {{command}} {{command_arguments}}`

- نوشتن PID در فایل مشخص:

`daemonize -p {{path/to/pidfile}} {{command}} {{command_arguments}}`

- استفاده از فایل قفل برای اطمینان از اجرای فقط یک نمونه در هر زمان:

`daemonize -l {{path/to/lockfile}} {{command}} {{command_arguments}}`

- استفاده از حساب کاربری مشخص:

`sudo daemonize -u {{user}} {{command}} {{command_arguments}}`
