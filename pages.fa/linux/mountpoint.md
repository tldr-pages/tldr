# mountpoint

> بررسی اینکه آیا دایرکتوری نقطهٔ اتصال فایل‌سیستم است.
> اطلاعات بیشتر: <https://manned.org/mountpoint>.

- بررسی نقطهٔ اتصال بودن دایرکتوری:

`mountpoint {{path/to/directory}}`

- بررسی نقطهٔ اتصال بودن دایرکتوری بدون نمایش خروجی:

`mountpoint {{[-q|--quiet]}} {{path/to/directory}}`

- نمایش شماره‌های اصلی و فرعی فایل‌سیستم نقطهٔ اتصال:

`mountpoint {{[-d|--fs-devno]}} {{path/to/directory}}`
