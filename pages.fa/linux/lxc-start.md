# lxc-start

> شروع کانتینر.
> اطلاعات بیشتر: <https://linuxcontainers.org/lxc/getting-started/>.

- شروع سرویس lxc:

`systemctl start lxc-net`

- شروع کانتینر:

`sudo lxc-start {{container_name}}`

- شروع کانتینر در پیش‌زمینه:

`sudo lxc-start {{container_name}} {{[-F|--foreground]}}`

- خروج از کانتینر پیش‌زمینه (این دستور را در ترمینال جداگانه اجرا کنید):

`sudo lxc-stop {{container_name}}`

- نوشتن گزارش‌های اشکال‌زدایی در فایل:

`sudo lxc-start {{container_name}} {{[-l|--logpriority]}} DEBUG {{[-o|--logfile]}} {{path/to/logfile}}`

- نمایش راهنما:

`lxc-start {{[-?|--help]}}`
