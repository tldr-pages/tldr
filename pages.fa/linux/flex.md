# flex

> تولیدکنندهٔ تحلیلگر واژگانی.
> با دریافت مشخصات یک تحلیلگر واژگانی، کد C پیاده‌ساز آن را تولید می‌کند.
> اطلاعات بیشتر: <https://manned.org/flex>.

- تولید تحلیلگر از فایل Lex و ذخیره در فایل `lex.yy.c`:

`flex {{analyzer.l}}`

- نوشتن تحلیلگر در خروجی استاندارد `stdout`:

`flex {{[-t|--stdout]}} {{analyzer.l}}`

- تعیین فایل خروجی:

`flex {{analyzer.l}} {{[-o|--outfile]}} {{analyzer.c}}`

- تولید پویشگر دسته‌ای به جای پویشگر تعاملی:

`flex {{[-B|--batch]}} {{analyzer.l}}`

- کامپایل فایل C تولیدشده توسط Lex:

`cc {{path/to/lex.yy.c}} -o {{executable}}`
