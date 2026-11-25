# cloud-init

> مدیریت مقداردهی اولیهٔ نمونهٔ ابری.
> اطلاعات بیشتر: <https://cloudinit.readthedocs.io/en/latest/reference/cli.html>.

- نمایش وضعیت آخرین اجرای cloud-init:

`cloud-init status`

- انتظار برای پایان اجرای cloud-init و سپس گزارش وضعیت:

`cloud-init status --wait`

- فهرست کردن کلیدهای فرادادهٔ سطح‌بالای موجود برای پرس‌وجو:

`cloud-init query --list-keys`

- پرس‌وجوی داده‌ها از فرادادهٔ ذخیره‌شدهٔ نمونه:

`cloud-init query {{dot_delimited_variable_path}}`

- پاکسازی گزارش‌ها و فایل‌های ایجادشده برای امکان اجرای مجدد cloud-init:

`cloud-init clean`
