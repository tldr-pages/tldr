# systemd-nspawn

> اجرای دستور یا سیستم‌عامل در کانتینر سبک.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-nspawn.html>.

- اجرای دستور در کانتینر:

`systemd-nspawn {{[-D|--directory]}} {{path/to/container_root}}`

- اجرای سیستم‌عامل کامل مبتنی بر لینوکس در کانتینر:

`systemd-nspawn {{[-b|--boot]}} {{[-D|--directory]}} {{path/to/container_root}}`

- اجرای دستور مشخص به‌عنوان PID 2 در کانتینر (به‌جای PID 1) با فرایند init واسط:

`systemd-nspawn {{[-D|--directory]}} {{path/to/container_root}} {{[-a|--as-pid2]}}`

- تعیین نام ماشین و نام میزبان:

`systemd-nspawn {{[-M|--machine]}} {{container_name}} --hostname {{container_host}} {{[-D|--directory]}} {{path/to/container_root}}`
