# trizen

> ابزار Arch Linux برای ساخت بسته‌ها از مخزن کاربری Arch (AUR).
> اطلاعات بیشتر: <https://github.com/trizen/trizen/blob/master/TRIZEN.md>.

- همگام‌سازی و به‌روزرسانی همهٔ بسته‌های AUR:

`trizen -Syua`

- نصب بستهٔ جدید:

`trizen -S {{package}}`

- حذف بسته و وابستگی‌های آن:

`trizen -Rs {{package}}`

- جست‌وجوی کلیدواژه در پایگاه دادهٔ بسته‌ها:

`trizen -Ss {{keyword}}`

- نمایش اطلاعات بسته:

`trizen -Si {{package}}`

- فهرست کردن بسته‌ها و نسخه‌های نصب‌شده:

`trizen -Qe`
