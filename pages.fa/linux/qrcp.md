# qrcp

> ابزار انتقال فایل.
> اطلاعات بیشتر: <https://github.com/claudiodangelis/qrcp#usage>.

- ارسال فایل یا دایرکتوری‌ها:

`qrcp send {{path/to/file_or_directory1 path/to/file_directory2 ...}}`

- دریافت فایل‌ها:

`qrcp receive`

- فشرده‌سازی محتوا پیش از انتقال:

`qrcp send --zip {{path/to/file_or_directory}}`

- استفاده از پورت مشخص:

`qrcp {{send|receive}} {{[-p|--port]}} {{port_number}}`

- استفاده از واسط شبکهٔ مشخص:

`qrcp {{send|receive}} {{[-i|--interface]}} {{interface}}`

- زنده نگه داشتن سرور:

`qrcp {{send|receive}} --keep-alive`
