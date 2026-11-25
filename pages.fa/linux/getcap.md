# getcap

> نمایش نام و قابلیت‌های هر فایل مشخص‌شده.
> اطلاعات بیشتر: <https://manned.org/getcap>.

- دریافت قابلیت‌های فایل‌های مشخص:

`getcap {{path/to/file1 path/to/file2 ...}}`

- دریافت بازگشتی قابلیت‌های همهٔ فایل‌های زیر دایرکتوری‌های مشخص:

`getcap -r {{path/to/directory1 path/to/directory2 ...}}`

- نمایش همهٔ موارد جست‌وجوشده حتی اگر قابلیتی تنظیم نشده باشد:

`getcap -v {{path/to/file1 path/to/file2 ...}}`
