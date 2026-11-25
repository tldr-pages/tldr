# pacgraph

> رسم نمودار بسته‌های نصب‌شده در PNG، SVG، رابط گرافیکی یا کنسول.
> اطلاعات بیشتر: <https://manned.org/pacgraph>.

- تولید نمودار SVG و PNG:

`pacgraph`

- تولید نمودار SVG:

`pacgraph {{[-s|--svg]}}`

- چاپ خلاصه در کنسول:

`pacgraph {{[-c|--console]}}`

- تعیین نام یا محل فایل به‌جای پیش‌فرض (توجه: پسوند فایل را مشخص نکنید):

`pacgraph {{[-f|--file]}} {{path/to/file}}`

- تغییر رنگ بسته‌هایی که وابستگی نیستند:

`pacgraph {{[-t|--top]}} {{color}}`

- تغییر رنگ وابستگی‌های بسته‌ها:

`pacgraph {{[-d|--dep]}} {{color}}`

- تغییر رنگ پس‌زمینهٔ نمودار:

`pacgraph {{[-b|--background]}} {{color}}`

- تغییر رنگ پیوندهای بین بسته‌ها:

`pacgraph {{[-l|--link]}} {{color}}`
