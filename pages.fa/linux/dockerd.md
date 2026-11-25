# dockerd

> فرایندی پایدار برای شروع و مدیریت کانتینرهای Docker.
> اطلاعات بیشتر: <https://docs.docker.com/reference/cli/dockerd/>.

- اجرای سرویس Docker:

`dockerd`

- اجرای سرویس Docker و پیکربندی آن برای گوش دادن به سوکت‌های مشخص یونیکس و TCP:

`dockerd {{[-H|--host]}} unix://{{path/to/tmp.sock}} {{[-H|--host]}} tcp://{{ip_address}}`

- اجرا با فایل PID مشخص سرویس:

`dockerd {{[-p|--pidfile]}} {{path/to/pid_file}}`

- اجرا در حالت اشکال‌زدایی:

`dockerd {{[-D|--debug]}}`

- اجرا و تنظیم سطح گزارش مشخص:

`dockerd {{[-l|--log-level]}} {{debug|info|warn|error|fatal}}`
