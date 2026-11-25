# fwupdmgr

> به‌روزرسانی میان‌افزار دستگاه‌ها، از جمله UEFI، با استفاده از `fwupd`.
> همچنین ببینید: `fwupdtool`.
> اطلاعات بیشتر: <https://github.com/fwupd/fwupd/blob/main/src/fwupdmgr.md>.

- نمایش همهٔ دستگاه‌های شناسایی‌شده توسط `fwupd`:

`fwupdmgr get-devices`

- دانلود آخرین فرادادهٔ میان‌افزار از LVFS:

`fwupdmgr refresh`

- فهرست کردن به‌روزرسانی‌های موجود برای دستگاه‌های سیستم:

`fwupdmgr get-updates`

- نصب به‌روزرسانی‌های میان‌افزار:

`fwupdmgr update`

- سوار کردن مجدد `/boot` با دسترسی بیشتر اگر به‌روزرسانی از فقط‌خواندنی بودن سیستم فایل شکایت کند:

`sudo mount {{[-o|--options]}} uid=1000,gid=1000,umask=0022 {{/dev/sdX}} /boot`

- نمایش تاریخچهٔ به‌روزرسانی میان‌افزار:

`fwupdmgr get-history`
