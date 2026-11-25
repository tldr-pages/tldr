# guix package

> نصب، ارتقا و حذف بسته‌های Guix یا بازگشت به پیکربندی‌های قبلی.
> اطلاعات بیشتر: <https://guix.gnu.org/manual/en/guix.html#Invoking-guix-package>.

- نصب بستهٔ جدید:

`guix package {{[-i|--install]}} {{package}}`

- حذف یک بسته:

`guix package {{[-r|--remove]}} {{package}}`

- جست‌وجوی عبارت منظم `regex` در پایگاه دادهٔ بسته‌ها:

`guix package {{[-s|--search]}} "{{search_pattern}}"`

- فهرست کردن بسته‌های نصب‌شده:

`guix package {{[-I|--list-installed]}}`

- فهرست کردن نسل‌ها:

`guix package {{[-l|--list-generations]}}`

- بازگشت به نسل قبلی:

`guix package --roll-back`
