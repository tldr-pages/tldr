# repo-add

> ابزار نگهداری پایگاه دادهٔ بسته که نصب بستهٔ مذکور با Pacman را ممکن می‌کند.
> همچنین : `repo-remove`.
> اطلاعات بیشتر: <https://manned.org/repo-add>.

- ایجاد مخزن خالی:

`repo-add {{path/to/database.db.tar.gz}}`

- افزودن بسته‌ها به مخزن:

`repo-add {{path/to/database.db.tar.gz}} {{package1.pkg.tar.zst package2.pkg.tar.zst ...}}`

- افزودن همهٔ بسته‌های دودویی دایرکتوری فعلی و حذف فایل‌های بستهٔ قدیمی:

`repo-add {{[-R|--remove]}} {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- افزودن همهٔ بسته‌های دودویی دایرکتوری فعلی در حالت بی‌صدا به‌جز پیام‌های هشدار و خطا:

`repo-add {{[-q|--quiet]}} {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- افزودن همهٔ بسته‌های دودویی دایرکتوری فعلی بدون نمایش رنگ:

`repo-add --nocolor {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`
