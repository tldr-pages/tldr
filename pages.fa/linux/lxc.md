# lxc

> مدیریت کانتینرهای لینوکس با REST API مربوط به lxd.
> می‌توان نام هر سرور راه دور را به ابتدای نام یا الگوی کانتینر اضافه کرد.
> اطلاعات بیشتر: <https://manned.org/lxc>.

- فهرست کردن کانتینرهای محلی مطابق رشته؛ برای فهرست کردن همهٔ کانتینرهای محلی رشته را حذف کنید:

`lxc list {{match_string}}`

- فهرست کردن تصاویر مطابق رشته؛ برای فهرست کردن همهٔ تصاویر رشته را حذف کنید:

`lxc image list [{{remote}}:]{{match_string}}`

- ایجاد کانتینر جدید از تصویر:

`lxc init [{{remote}}:]{{image}} {{container}}`

- شروع کانتینر:

`lxc start [{{remote}}:]{{container}}`

- توقف کانتینر:

`lxc stop [{{remote}}:]{{container}}`

- نمایش اطلاعات مفصل کانتینر:

`lxc info [{{remote}}:]{{container}}`

- گرفتن snapshot از کانتینر:

`lxc snapshot [{{remote}}:]{{container}} {{snapshot}}`

- اجرای دستور مشخص داخل کانتینر:

`lxc exec [{{remote}}:]{{container}} {{command}}`
