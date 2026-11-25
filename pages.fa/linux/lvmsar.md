# lvmsar

> گزارشگر فعالیت سیستم LVM.
> در LVM2 پشتیبانی نمی‌شود؛ `dmstats` ترجیح دارد.
> اطلاعات بیشتر: <https://manned.org/lvmsar>.

- اجرای گزارشگر قدیمی (فقط سیستم‌های LVM1):

`lvmsar`

- گزارش آمار ورودی/خروجی دستگاه با آمار device-mapper:

`dmstats report {{/dev/mapper/device}}`

- فهرست کردن ناحیه‌های آماری دستگاه:

`dmstats list {{/dev/mapper/device}}`
