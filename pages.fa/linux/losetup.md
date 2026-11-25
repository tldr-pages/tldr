# losetup

> راه‌اندازی و کنترل دستگاه‌های loop.
> اطلاعات بیشتر: <https://manned.org/losetup>.

- فهرست کردن دستگاه‌های loop با اطلاعات مفصل:

`losetup {{[-a|--all]}}`

- اتصال فایل به دستگاه loop مشخص:

`sudo losetup {{/dev/loop}} /{{path/to/file}}`

- اتصال فایل به دستگاه loop آزاد جدید و پویش پارتیشن‌های دستگاه:

`sudo losetup --show {{[-P|--partscan]}} {{[-f|--find]}} /{{path/to/file}}`

- اتصال فایل به دستگاه loop فقط‌خواندنی:

`sudo losetup {{[-r|--read-only]}} {{/dev/loop}} /{{path/to/file}}`

- جدا کردن همهٔ دستگاه‌های loop:

`sudo losetup {{[-D|--detach-all]}}`

- جدا کردن دستگاه loop مشخص:

`sudo losetup {{[-d|--detach]}} {{/dev/loop}}`
