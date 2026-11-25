# pmount

> سوار کردن دستگاه‌های قابل اتصال در حین کار با کاربر عادی.
> اطلاعات بیشتر: <https://manned.org/pmount>.

- سوار کردن دستگاه زیر `/media/` (با استفاده از دستگاه به‌عنوان نقطهٔ اتصال):

`pmount {{/dev/to/block/device}}`

- سوار کردن دستگاه با نوع فایل‌سیستم مشخص در `/media/label`:

`pmount {{[-t|--type]}} {{filesystem}} {{/dev/to/block/device}} {{label}}`

- سوار کردن CD-ROM (فایل‌سیستم ISO9660) در حالت فقط‌خواندنی:

`pmount {{[-t|--type]}} iso9660 {{[-r|--read-only]}} {{/dev/cdrom}}`

- سوار کردن دیسک قالب‌بندی‌شده با NTFS و اجبار دسترسی خواندن و نوشتن:

`pmount {{[-t|--type]}} ntfs {{[-w|--read-write]}} {{/dev/sdX}}`

- نمایش همهٔ دستگاه‌های جداشدنی سوارشده:

`pmount`
