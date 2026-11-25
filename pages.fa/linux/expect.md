# expect

> اجراکنندهٔ اسکریپت که با برنامه‌های نیازمند ورودی کاربر تعامل می‌کند.
> اطلاعات بیشتر: <https://manned.org/expect>.

- اجرای اسکریپت expect از یک فایل:

`expect {{path/to/file}}`

- اجرای اسکریپت expect مشخص:

`expect -c "{{commands}}"`

- ورود به REPL تعاملی با `-i` (برای خروج از `exit` یا `<Ctrl d>` استفاده کنید):

`expect -i`
