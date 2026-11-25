# woeusb

> ابزار ایجاد رسانهٔ Windows.
> اطلاعات بیشتر: <https://manned.org/woeusb>.

- قالب‌بندی USB و سپس ایجاد درایو نصب قابل راه‌اندازی Windows:

`sudo woeusb {{[-d|--device]}} {{path/to/windows.iso}} {{/dev/sdX}}`

- کپی فایل‌های Windows در پارتیشن موجود دستگاه ذخیره‌سازی USB و قابل راه‌اندازی کردن آن بدون پاک کردن داده‌های فعلی:

`woeusb {{[-p|--partition]}} {{path/to/windows.iso}} {{/dev/sdXN}}`
