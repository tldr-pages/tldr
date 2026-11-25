# pactree

> نمایشگر درخت وابستگی بسته برای pacman.
> اطلاعات بیشتر: <https://manned.org/pactree>.

- چاپ درخت وابستگی بستهٔ مشخص:

`pactree {{package}}`

- چاپ بسته‌هایی که به بستهٔ مشخص وابسته‌اند:

`pactree {{[-r|--reverse]}} {{package}}`

- چاپ وابستگی‌ها هرکدام در یک خط، بدون موارد تکراری:

`pactree {{[-u|--unique]}} {{package}}`

- گنجاندن وابستگی‌های اختیاری بستهٔ مشخص و رنگی کردن خروجی:

`pactree {{[-co|--color --optional]}} {{package}}`

- نمایش راهنما:

`pactree`
