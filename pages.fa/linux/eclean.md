# eclean

> پاکسازی فایل‌های منبع مخزن و بسته‌های دودویی.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Eclean>.

- پاکسازی دایرکتوری فایل‌های منبع:

`sudo eclean distfiles`

- پاکسازی دایرکتوری بسته‌های دودویی:

`sudo eclean packages`

- پاکسازی فایل‌های توزیع همهٔ بسته‌های نصب‌نشده با حفظ فایل‌های توزیع بسته‌های نصب‌شده:

`sudo eclean {{[-d|--deep]}} {{[-n|--package-names]}} distfiles`

- پاکسازی بسته‌های دودویی همهٔ بسته‌های نصب‌نشده با حفظ فایل‌های دودویی بسته‌های نصب‌شده:

`sudo eclean {{[-d|--deep]}} {{[-n|--package-names]}} packages`
