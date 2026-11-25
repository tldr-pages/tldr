# sysctl

> فهرست کردن و تغییر متغیرهای زمان اجرای هسته.
> اطلاعات بیشتر: <https://manned.org/sysctl.8>.

- نمایش همهٔ متغیرهای موجود و مقادیر آن‌ها:

`sysctl {{[-a|--all]}}`

- تنظیم متغیر وضعیت قابل تغییر هسته:

`sysctl {{[-w|--write]}} {{section.tunable}}={{value}}`

- دریافت شناسه‌های فایل باز فعلی:

`sysctl fs.file-nr`

- دریافت محدودیت فایل‌های هم‌زمان باز:

`sysctl fs.file-max`

- دریافت مقدار هر متغیر زمان اجرا:

`sysctl {{variable_name}}`

- چاپ فقط مقدار بدون نام متغیر:

`sysctl {{[-n|--values]}} {{variable_name}}`

- اعمال تغییرات از `/etc/sysctl.conf`:

`sysctl {{[-p|--load]}}`
