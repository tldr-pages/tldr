# pgrep

> یافتن یا ارسال سیگنال به فرایندها با نام.
> همچنین : `pidof`.
> اطلاعات بیشتر: <https://manned.org/pgrep>.

- بازگرداندن PID فرایندهای در حال اجرا با رشتهٔ دستور مطابق:

`pgrep {{process_name}}`

- نمایش دستور کامل نیز:

`pgrep {{[-a|--list-full]}} {{process_name}}`

- جست‌وجوی فرایندها همراه با گزینه‌های خط فرمان آن‌ها:

`pgrep {{[-f|--full]}} "{{process_name}} {{parameter}}"`

- جست‌وجوی فرایندهای اجراشده توسط کاربر مشخص:

`pgrep {{[-u|--euid]}} {{username}} {{process_name}}`
