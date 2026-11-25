# rc-service

> یافتن و اجرای سرویس‌های OpenRC با آرگومان‌ها.
> همچنین : `openrc`.
> اطلاعات بیشتر: <https://manned.org/rc-service>.

- نمایش وضعیت سرویس:

`rc-service {{service_name}} status`

- شروع سرویس:

`sudo rc-service {{service_name}} start`

- توقف سرویس:

`sudo rc-service {{service_name}} stop`

- راه‌اندازی مجدد سرویس:

`sudo rc-service {{service_name}} restart`

- شبیه‌سازی اجرای دستور دلخواه سرویس:

`sudo rc-service {{[-Z|--dry-run]}} {{service_name}} {{command_name}}`

- اجرای واقعی دستور دلخواه سرویس:

`sudo rc-service {{service_name}} {{command_name}}`

- یافتن محل تعریف سرویس روی دیسک:

`sudo rc-service {{[-r|--resolve]}} {{service_name}}`
