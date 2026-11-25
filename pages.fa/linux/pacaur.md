# pacaur

> ابزاری در Arch Linux برای ساخت و نصب بسته‌ها از مخزن کاربری Arch.
> اطلاعات بیشتر: <https://github.com/rmarquis/pacaur#name>.

- همگام‌سازی و به‌روزرسانی همهٔ بسته‌ها (از جمله AUR):

`pacaur -Syu`

- همگام‌سازی و به‌روزرسانی فقط بسته‌های AUR:

`pacaur -Syua`

- نصب بستهٔ جدید (از جمله AUR):

`pacaur -S {{package}}`

- حذف بسته و وابستگی‌های آن (از جمله بسته‌های AUR):

`pacaur -Rs {{package}}`

- جست‌وجوی کلیدواژه در پایگاه دادهٔ بسته‌ها (از جمله AUR):

`pacaur -Ss {{keyword}}`

- فهرست کردن همهٔ بسته‌های نصب‌شدهٔ فعلی (از جمله AUR):

`pacaur -Qs`
