# eix

> ابزارهایی برای جست‌وجوی بسته‌های محلی جنتو.
> حافظهٔ نهان محلی بسته‌ها را با `eix-update` به‌روزرسانی کنید.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Eix>.

- جست‌وجوی یک بسته:

`eix {{query}}`

- جست‌وجوی بسته‌های نصب‌شده:

`eix --installed {{query}}`

- جست‌وجو در توضیحات بسته‌ها:

`eix --description "{{description}}"`

- جست‌وجو بر اساس مجوز بسته:

`eix --license {{license}}`

- کنار گذاشتن نتایج از جست‌وجو:

`eix --not --license {{license}}`
