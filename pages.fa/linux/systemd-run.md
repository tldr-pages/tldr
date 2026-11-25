# systemd-run

> اجرای برنامه‌ها در واحدهای scope یا سرویس موقت یا واحدهای سرویس فعال‌شده با مسیر، سوکت یا زمان‌سنج.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-run.html>.

- شروع سرویس موقت:

`sudo systemd-run {{command}} {{argument1 argument2 ...}}`

- شروع سرویس موقت تحت مدیر سرویس کاربر فعلی (بدون دسترسی ویژه):

`systemd-run --user {{command}} {{argument1 argument2 ...}}`

- شروع سرویس موقت با نام و توضیح دلخواه واحد:

`sudo systemd-run {{[-u|--unit]}} {{name}} --description {{string}} {{command}} {{argument1 argument2 ...}}`

- شروع سرویس موقتی که پس از پایان پاک‌سازی نشود، با متغیر محیطی دلخواه:

`sudo systemd-run {{[-r|--remain-after-exit]}} {{[-E|--setenv]}} {{name}}={{value}} {{command}} {{argument1 argument2 ...}}`

- شروع زمان‌سنج موقت که سرویس موقت خود را دوره‌ای اجرا می‌کند (برای قالب رویداد تقویمی `man systemd.time` را ببینید):

`sudo systemd-run --on-calendar={{calendar_event}} {{command}} {{argument1 argument2 ...}}`

- اشتراک ترمینال با برنامه (با اجازهٔ ورودی/خروجی تعاملی) و حفظ جزئیات اجرا پس از خروج برنامه:

`systemd-run {{[-r|--remain-after-exit]}} --pty {{command}}`

- تنظیم ویژگی‌های فرایند (مانند CPUQuota، MemoryMax) و انتظار تا خروج آن:

`systemd-run {{[-p|--property]}} MemoryMax={{memory_in_bytes}} {{[-p|--property]}} CPUQuota={{percentage_of_cpu_time}}% --wait {{command}}`

- استفاده از برنامه در خط لولهٔ پوسته:

`{{command1}} | systemd-run {{[-P|--pipe]}} {{command2}} | {{command3}}`
