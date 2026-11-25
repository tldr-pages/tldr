# pamac

> ابزار خط فرمان مدیر بستهٔ گرافیکی pamac.
> اگر بسته‌های AUR را نمی‌بینید، آن را در `/etc/pamac.conf` یا رابط گرافیکی فعال کنید.
> اطلاعات بیشتر: <https://wiki.manjaro.org/index.php/Pamac>.

- نصب بستهٔ جدید:

`pamac install {{package_name}}`

- حذف بسته و وابستگی‌های دیگر غیرضروری آن (یتیم‌ها):

`pamac remove --orphans {{package_name}}`

- جست‌وجوی بسته در پایگاه دادهٔ بسته‌ها:

`pamac search {{package_name}}`

- فهرست کردن بسته‌های نصب‌شده:

`pamac list --installed`

- بررسی به‌روزرسانی بسته‌ها:

`pamac checkupdates`

- ارتقای همهٔ بسته‌ها:

`pamac upgrade`
