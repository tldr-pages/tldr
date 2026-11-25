# fscrypt

> ابزار Go برای مدیریت رمزگذاری سیستم فایل لینوکس.
> اطلاعات بیشتر: <https://github.com/google/fscrypt#example-usage>.

- آماده‌سازی سیستم فایل ریشه برای استفاده با `fscrypt`:

`sudo fscrypt setup`

- آماده‌سازی نقطهٔ اتصال مشخص برای استفاده با `fscrypt`:

`fscrypt setup {{path/to/directory}}`

- فعال کردن رمزگذاری سیستم فایل برای یک دایرکتوری:

`fscrypt encrypt {{path/to/directory}}`

- باز کردن قفل دایرکتوری رمزگذاری‌شده:

`fscrypt unlock {{path/to/encrypted_directory}}`

- قفل کردن دایرکتوری رمزگذاری‌شده:

`fscrypt lock {{path/to/encrypted_directory}}`
