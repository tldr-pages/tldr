# aurman

> ابزاری در آرچ لینوکس برای ساخت و نصب بسته‌ها از مخزن کاربران آرچ.
> همچنین : `pacman`.
> اطلاعات بیشتر: <https://github.com/polygamma/aurman#syntax>.

- همگام‌سازی و به‌روزرسانی همهٔ بسته‌ها:

`aurman {{[-S|--sync]}} {{[-y|--refresh]}} {{[-u|--sysupgrade]}}`

- همگام‌سازی و به‌روزرسانی همهٔ بسته‌ها بدون نمایش تغییرات فایل‌های `PKGBUILD`:

`aurman {{[-S|--sync]}} {{[-y|--refresh]}} {{[-u|--sysupgrade]}} --noedit`

- نصب یک بستهٔ جدید:

`aurman {{[-S|--sync]}} {{package}}`

- نصب یک بستهٔ جدید بدون نمایش تغییرات فایل‌های `PKGBUILD`:

`aurman {{[-S|--sync]}} --noedit {{package}}`

- نصب یک بستهٔ جدید بدون درخواست تأیید:

`aurman {{[-S|--sync]}} --noedit --noconfirm {{package}}`

- جست‌وجوی یک کلیدواژه در پایگاه دادهٔ بسته‌ها از مخازن رسمی و AUR:

`aurman {{[-S|--sync]}} {{[-s|--search]}} {{keyword}}`

- حذف یک بسته و وابستگی‌های آن:

`aurman --remove --recursive --nosave {{package}}`

- پاکسازی حافظهٔ نهان بسته‌ها (برای پاکسازی همهٔ بسته‌ها از دو گزینهٔ `--clean` استفاده کنید):

`aurman {{[-S|--sync]}} {{[-c|--clean]}}`
