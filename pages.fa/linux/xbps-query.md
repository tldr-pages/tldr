# xbps-query

> ابزار XBPS برای پرس‌وجوی اطلاعات بسته‌ها و مخازن.
> همچنین ببینید: `xbps`.
> اطلاعات بیشتر: <https://manned.org/xbps-query>.

- جست‌وجوی بسته در مخازن راه دور با `regex` یا کلیدواژه (اگر `--regex` حذف شود):

`xbps-query {{[-s|--search]}} {{regex|keyword}} --repository --regex`

- نمایش اطلاعات بستهٔ نصب‌شده:

`xbps-query {{[-S|--show]}} {{package}}`

- نمایش اطلاعات بسته‌ای در مخازن راه دور:

`xbps-query {{[-S|--show]}} {{package}} --repository`

- فهرست کردن بسته‌های ثبت‌شده در پایگاه دادهٔ بسته:

`xbps-query {{[-l|--list-pkgs]}}`

- فهرست کردن بسته‌های صریحاً نصب‌شده (نه نصب‌شده به‌صورت خودکار به‌عنوان وابستگی):

`xbps-query {{[-m|--list-manual-pkgs]}}`
