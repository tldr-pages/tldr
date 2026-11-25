# pkgtool

> ابزار تعاملی مبتنی بر منو برای مدیریت بسته‌های Slackware.
> همچنین ببینید: `installpkg`, `removepkg`, `upgradepkg`, `makepkg`.
> اطلاعات بیشتر: <https://www.slackbook.org/html/book.html#PACKAGE-MANAGEMENT-PACKAGE-UTILITIES-PKGTOOL>.

- اجرای ابزار تعاملی بسته:

`sudo pkgtool`

- حذف تعاملی بسته‌ها:

`sudo pkgtool --remove_menu`

- مشاهدهٔ بسته‌های نصب‌شده:

`pkgtool --view_menu`

- نصب بسته‌ها از دایرکتوری فعلی:

`sudo pkgtool --install_menu`

- راه‌اندازی تعاملی بسته‌ها (اجرای اسکریپت‌های `doinst.sh`):

`sudo pkgtool --setup_menu`
