# logger

> افزودن پیام به گزارش سیستم.
> اطلاعات بیشتر: <https://manned.org/logger>.

- ثبت پیام در syslog:

`logger {{message}}`

- دریافت ورودی از `stdin` و ثبت در syslog:

`echo {{log_entry}} | logger`

- ارسال خروجی به سرور syslog راه دور روی پورت مشخص؛ پورت پیش‌فرض ۵۱۴ است:

`echo {{log_entry}} | logger {{[-n|--server]}} {{hostname}} {{[-P|--port]}} {{port}}`

- استفاده از برچسب مشخص برای هر خط ثبت‌شده؛ پیش‌فرض نام کاربر واردشده است:

`echo {{log_entry}} | logger {{[-t|--tag]}} {{tag}}`

- ثبت پیام‌ها با اولویت مشخص؛ پیش‌فرض `user.notice` است. برای همهٔ گزینه‌های اولویت `man logger` را ببینید:

`echo {{log_entry}} | logger {{[-p|--priority]}} {{user.warning}}`
