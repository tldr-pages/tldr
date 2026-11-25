# ptyxis

> ترمینال مبتنی بر کانتینر برای GNOME.
> اطلاعات بیشتر: <https://gitlab.gnome.org/chergert/ptyxis#basic-usage--command-line-options>.

- باز کردن پنجرهٔ جدید Ptyxis:

`ptyxis --new-window`

- اجرای دستور مشخص در پنجرهٔ ترمینال جدید:

`ptyxis {{[-x|--execute]}} {{command}}`

- باز کردن زبانهٔ جدید در آخرین پنجرهٔ بازشده:

`ptyxis --tab`

- تنظیم عنوان برای پنجره یا زبانهٔ جدید:

`ptyxis --tab {{[-T|--title]}} {{title}}`

- تعیین دایرکتوری کاری برای زبانه، پنجره یا اجرای دستور جدید:

`ptyxis {{[-d|--working-directory]}} {{path/to/directory}} --tab`
