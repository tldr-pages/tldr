# emerge

> ابزار مدیریت بستهٔ جنتو لینوکس.
> برای دستورهای معادل در دیگر مدیران بسته، <https://wiki.archlinux.org/title/Pacman/Rosetta> را ببینید.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Portage#emerge>.

- همگام‌سازی همهٔ بسته‌ها:

`sudo emerge --sync`

- به‌روزرسانی همهٔ بسته‌ها، شامل وابستگی‌ها:

`sudo emerge {{[-avuDN|--ask --verbose --update --deep --newuse]}} @world`

- ادامهٔ یک به‌روزرسانی ناموفق با رد کردن بستهٔ ناموفق:

`sudo emerge --resume --skipfirst`

- نصب بستهٔ جدید با درخواست تأیید:

`sudo emerge {{[-av|--ask --verbose]}} {{package}}`

- حذف یک بسته و وابستگی‌های آن با درخواست تأیید:

`sudo emerge {{[-avc|--ask --verbose --depclean]}} {{package}}`

- حذف بسته‌های یتیم (نصب‌شده به‌عنوان وابستگی اما دیگر مورد نیاز هیچ بسته‌ای نیستند):

`sudo emerge {{[-avc|--ask --verbose --depclean]}}`

- جست‌وجوی یک کلیدواژه در پایگاه دادهٔ بسته‌ها:

`emerge {{[-S|--searchdesc]}} {{keyword}}`
