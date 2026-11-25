# logsave

> ذخیرهٔ خروجی دستور در فایل گزارش.
> اطلاعات بیشتر: <https://manned.org/logsave>.

- اجرای دستور با آرگومان‌های مشخص و ذخیرهٔ خروجی آن در فایل گزارش:

`logsave {{path/to/logfile}} {{command}}`

- دریافت ورودی از `stdin` و ذخیره در فایل گزارش:

`logsave {{logfile}} -`

- افزودن خروجی به فایل گزارش به‌جای جایگزینی محتوای فعلی:

`logsave -a {{logfile}} {{command}}`

- نمایش خروجی مفصل:

`logsave -v {{logfile}} {{command}}`
