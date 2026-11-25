# systemd-delta

> یافتن فایل‌های پیکربندی مرتبط با systemd که بازنویسی شده‌اند.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-delta.html>.

- نمایش همهٔ فایل‌های پیکربندی بازنویسی‌شده:

`systemd-delta`

- نمایش فقط فایل‌های انواع مشخص (فهرست جداشده با ویرگول):

`systemd-delta {{[-t|--type]}} {{masked|equivalent|redirected|overridden|extended|unchanged}}`

- نمایش فقط فایل‌هایی که مسیرشان با پیشوند مشخص شروع می‌شود (پیشوند دایرکتوری حاوی زیردایرکتوری‌های فایل پیکربندی systemd است):

`systemd-delta {{/etc|/run|/usr/lib|...}}`

- محدود کردن بیشتر مسیر جست‌وجو با افزودن پسوند (پیشوند اختیاری است):

`systemd-delta {{prefix}}/{{tmpfiles.d|sysctl.d|systemd/system|...}}`
