# systemd-dissect

> بررسی و تعامل با تصاویر دیسک سیستم‌عامل، به‌ویژه تصاویر دیسک قابل کشف (DDI).
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-dissect.html>.

- نمایش اطلاعات کلی تصویر سیستم‌عامل:

`systemd-dissect {{path/to/image.raw}}`

- سوار کردن تصویر سیستم‌عامل:

`systemd-dissect {{[-m|--mount]}} {{path/to/image.raw}} {{/mnt/image}}`

- پیاده کردن تصویر سیستم‌عامل:

`systemd-dissect {{[-u|--umount]}} {{/mnt/image}}`

- فهرست کردن فایل‌های تصویر:

`systemd-dissect {{[-l|--list]}} {{path/to/image.raw}}`

- اتصال تصویر سیستم‌عامل به دستگاه بلوکی loopback تخصیص‌یافتهٔ خودکار و چاپ مسیر آن:

`systemd-dissect --attach {{path/to/image.raw}}`

- جدا کردن تصویر سیستم‌عامل از دستگاه بلوکی loopback:

`systemd-dissect --detach {{path/to/device}}`
