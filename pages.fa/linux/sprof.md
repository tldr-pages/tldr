# sprof

> خواندن و نمایش داده‌های نمایه‌گیری شیء مشترک.
> توجه: به داده‌های نمایهٔ تولیدشده از طریق متغیر محیطی `$LD_PROFILE` نیاز دارد.
> اطلاعات بیشتر: <https://manned.org/sprof>.

- تولید نمایهٔ تخت و گراف فراخوانی (خروجی پیش‌فرض):

`sprof {{path/to/library.so}} {{path/to/library.so.profile}}`

- تولید نمایهٔ تخت با شمارش و tickها:

`sprof {{[-p|--flat-profile]}} {{path/to/library.so}} {{path/to/library.so.profile}}`

- تولید گراف فراخوانی:

`sprof {{[-q|--graph]}} {{path/to/library.so}} {{path/to/library.so.profile}}`

- چاپ جفت‌های فراخوانی و تعداد استفادهٔ آن‌ها:

`sprof {{[-c|--call-pairs]}} {{path/to/library.so}} {{path/to/library.so.profile}}`

- استفاده از داده‌های نمایهٔ دایرکتوری فعلی (تشخیص خودکار با soname):

`sprof {{path/to/library.so}}`
