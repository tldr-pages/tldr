# pacreport

> تولید گزارش بسته‌های نصب‌شده.
> اطلاعات بیشتر: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacreport.pod>.

- تولید خلاصهٔ بسته‌های نصب‌شده:

`pacreport`

- فهرست کردن فایل‌های بدون مالک:

`pacreport --unowned-files`

- فهرست کردن فایل‌های گمشدهٔ بسته‌ها:

`pacreport --missing-files`

- جست‌وجوی فایل‌های پشتیبان ادغام‌نشده (مانند `.pacnew` و `.pacsave`) در `/etc`:

`pacreport --backups`

- نمایش بسته‌های گروه مشخص که اکنون نصب نشده‌اند:

`pacreport --group {{group_name}}`
