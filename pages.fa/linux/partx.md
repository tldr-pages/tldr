# partx

> تجزیهٔ جدول پارتیشن و اطلاع دادن آن به هسته.
> اطلاعات بیشتر: <https://manned.org/partx>.

- فهرست کردن پارتیشن‌های دستگاه بلوکی یا تصویر دیسک:

`sudo partx {{[-l|--list]}} {{path/to/device_or_disk_image}}`

- افزودن همهٔ پارتیشن‌های یافت‌شده در دستگاه بلوکی مشخص به هسته:

`sudo partx {{[-a|--add]}} {{[-v|--verbose]}} {{path/to/device_or_disk_image}}`

- حذف همهٔ پارتیشن‌های یافت‌شده از هسته (پارتیشن‌های دیسک تغییر نمی‌کنند):

`sudo partx {{[-d|--delete]}} {{path/to/device_or_disk_image}}`
