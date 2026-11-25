# systemctl list-paths

> فهرست کردن واحدهای مسیر موجود در حافظه، مرتب‌شده بر اساس مسیر.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-paths%20PATTERN%E2%80%A6>.

- نمایش همهٔ واحدهای مسیر موجود در حافظه:

`systemctl list-paths`

- فهرست کردن واحدهای مسیر مطابق الگوی wildcard مشخص یعنی `glob`:

`systemctl list-paths {{pattern}}`

- فهرست کردن واحدهای مسیر مطابق چند الگو:

`systemctl list-paths {{pattern_1 pattern_2 ...}}`

- نمایش همهٔ واحدهای مسیر، از جمله موارد غیرفعال:

`systemctl list-paths {{[-a|--all]}}`

- فیلتر واحدهای مسیر بر اساس وضعیت:

`systemctl list-paths --state {{state}}`

- نمایش انواع واحدها در خروجی نیز:

`systemctl list-paths --show-types`
