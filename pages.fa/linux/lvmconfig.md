# lvmconfig

> نمایش و تغییر اطلاعات پیکربندی LVM.
> اطلاعات بیشتر: <https://manned.org/lvmconfig>.

- نمایش پیکربندی مؤثر در حال استفاده (پس از ادغام همهٔ منابع پیکربندی):

`lvmconfig --typeconfig current --mergedconfig`

- نمایش فقط تنظیماتی که با مقادیر پیش‌فرض تفاوت دارند:

`lvmconfig --typeconfig diff`

- فهرست کردن همهٔ کلیدهای پیکربندی:

`lvmconfig {{[-l|--list]}}`

- چاپ پیکربندی پیش‌فرض با توضیحات کامل و فاصله‌گذاری اضافی:

`lvmconfig --typeconfig default --withcomments --withspaces`

- اعتبارسنجی کل پیکربندی ادغام‌شده و گزارش خطاها:

`lvmconfig --mergedconfig --validate`

- نوشتن پیکربندی مؤثر فعلی در فایل:

`lvmconfig --typeconfig current {{[-f|--file]}} {{path/to/output.conf}}`
