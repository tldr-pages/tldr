# umount

> جدا کردن فایل‌سیستم از نقطهٔ اتصال آن و غیرقابل دسترس کردن آن.
> فایل‌سیستم مشغول را نمی‌توان پیاده کرد.
> اطلاعات بیشتر: <https://manned.org/umount.8>.

- پیاده کردن فایل‌سیستم با ارسال مسیر مبدأ اتصال:

`sudo umount {{path/to/device_file}}`

- پیاده کردن فایل‌سیستم با ارسال مسیر مقصد اتصال:

`sudo umount {{path/to/mounted_directory}}`

- در صورت شکست پیاده‌سازی، تلاش برای سوار کردن مجدد فایل‌سیستم به‌صورت فقط‌خواندنی:

`sudo umount {{[-r|--read-only]}} {{path/to/mounted_directory}}`

- پیاده کردن بازگشتی هر دایرکتوری مشخص:

`sudo umount {{[-R|--recursive]}} {{path/to/mounted_directory}}`

- پیاده کردن همهٔ فایل‌سیستم‌های سوارشده (به‌جز فایل‌سیستم `proc`):

`sudo umount {{[-a|--all]}}`

- جدا کردن فایل‌سیستم از سلسله‌مراتب فایل‌سیستم و پیاده کردن آن به‌محض نبود ارجاع:

`sudo umount {{[-l|--lazy]}} {{path/to/mounted_directory}}`
