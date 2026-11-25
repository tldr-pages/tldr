# systemctl kill

> ارسال سیگنال به یک یا چند فرایند واحد.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#kill%20PATTERN%E2%80%A6>.

- ارسال سیگنال `SIGTERM` به واحد برای پایان دادن به آن:

`systemctl kill {{unit}}`

- ارسال سیگنال مشخص به واحد:

`systemctl kill {{[-s|--signal]}} {{signal_number|signal_name}} {{unit}}`

- ارسال سیگنال `SIGHUP` فقط به فرایند اصلی واحد:

`systemctl kill {{[-s|--signal]}} {{[1|SIGHUP]}} --kill-whom main {{unit}}`

- فهرست کردن همهٔ سیگنال‌های موجود:

`systemctl kill {{[-s|--signal]}} help`
