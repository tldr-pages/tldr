# systemctl list-dependencies

> نمایش درخت وابستگی واحد در systemd.
> همچنین : `systemctl list-units`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-dependencies%20UNIT%E2%80%A6>.

- نمایش درخت وابستگی `default.target`:

`systemctl list-dependencies`

- نمایش درخت وابستگی واحد مشخص:

`systemctl list-dependencies {{unit}}`

- گنجاندن همهٔ انواع وابستگی (نه فقط `Requires=` و `Wants=`):

`systemctl list-dependencies {{unit}} {{[-a|--all]}}`

- محدود کردن درخت به نوع واحد مشخص:

`systemctl list-dependencies {{unit}} {{[-t|--type]}} {{service|socket|target|mount|...}}`

- معکوس کردن جهت برای نمایش واحدهای وابسته به واحد مشخص:

`systemctl list-dependencies {{unit}} --reverse`

- چاپ خروجی بدون سربرگ یا پانوشت (برای اسکریپت‌ها):

`systemctl list-dependencies {{unit}} --no-legend`
