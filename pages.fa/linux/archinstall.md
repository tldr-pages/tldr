# archinstall

> نصب‌کنندهٔ گام‌به‌گام آرچ لینوکس.
> اطلاعات بیشتر: <https://archinstall.archlinux.page/installing/guided.html>.

- شروع نصب‌کنندهٔ تعاملی:

`archinstall`

- شبیه‌سازی نصب با طی مراحل نصب‌کنندهٔ تعاملی و تولید فایل پیکربندی بدون نصب:

`archinstall --dry-run`

- فعال کردن گزینه‌های پیشرفته:

`archinstall --advanced`

- نصب با استفاده از فایل‌های پیکربندی مشخص‌شده:

`archinstall --config {{path/to/config.json}} --creds {{path/to/credentials.json}}`

- نصب با استفاده از فایل‌های پیکربندی از یک سرور راه دور:

`archinstall --config-url {{https://example.com/config.json}} --creds-url {{https://example.com/credentials.json}}`

- نصب با استفاده از اسکریپت مشخص‌شده:

`archinstall --script {{minimal|only_hd}}`
