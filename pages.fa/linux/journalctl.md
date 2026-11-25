# journalctl

> پرس‌وجو از گزارش systemd.
> همچنین ببینید: `dmesg`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/journalctl.html>.

- نمایش آخرین `n` خط و دنبال کردن پیام‌های جدید (مانند `tail --follow` برای syslog سنتی):

`journalctl {{[-n|--lines]}} {{n}} {{[-f|--follow]}}`

- نمایش همهٔ پیام‌های سطح اولویت ۳ (خطاها) از راه‌اندازی پیش از آخرین خاموشی:

`journalctl {{[-b|--boot]}} -1 {{[-p|--priority]}} 3`

- نمایش همهٔ پیام‌های واحد مشخص:

`journalctl {{[-u|--unit]}} {{unit}}`

- نمایش گزارش‌های واحد مشخص از آخرین شروع آن:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID {{unit}})`

- فیلتر کردن پیام‌ها در بازهٔ زمانی (برچسب زمانی یا مقادیری مانند «yesterday»):

`journalctl {{[-S|--since]}} {{now|today|yesterday|tomorrow|...}} {{[-U|--until]}} "{{YYYY-MM-DD HH:MM:SS}}"`

- نمایش همهٔ پیام‌های فرایند مشخص:

`journalctl _PID={{process_id}}`

- نمایش همهٔ پیام‌های فایل اجرایی مشخص:

`journalctl {{path/to/executable}}`

- حذف گزارش‌های قدیمی‌تر از ۲ روز:

`journalctl --vacuum-time 2d`
