# run_init

> اجرای اسکریپت‌های init در زمینهٔ مناسب SELinux.
> معمولاً برای اجرای اسکریپت‌های سرویس سیستم با دامنه‌های صحیح SELinux استفاده می‌شود.
> همچنین ببینید: `runcon`, `semanage`.
> اطلاعات بیشتر: <https://manned.org/run_init>.

- اجرای اسکریپت در زمینهٔ اسکریپت init:

`sudo run_init {{path/to/script}}`

- اجرای اسکریپت با آرگومان‌ها:

`sudo run_init {{path/to/script}} {{start|stop|restart}}`

- اجرای اسکریپت و تعیین صریح زمینهٔ اسکریپت init:

`sudo run_init {{[-t|--type]}} {{context_type}} {{path/to/script}}`

- شبیه‌سازی اجرای اسکریپت و نمایش زمینه‌ای که استفاده خواهد شد:

`sudo run_init {{[-n|--dry-run]}} {{path/to/script}}`
