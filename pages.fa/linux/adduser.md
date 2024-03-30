# adduser

> ابزار اضافه‌ کردن کاربر.
> اطلاعات بیشتر: <https://manpages.debian.org/latest/adduser/adduser.html>.

- ایجاد یک کاربر جدید با دایرکتوری خانگی پیش‌فرض و درخواست از کاربر برای تنظیم رمز عبور:

`adduser {{username}}`

- ایجاد یک کاربر جدید بدون دایرکتوری خانگی:

`adduser --no-create-home {{username}}`

- ایجاد یک کاربر جدید با دایرکتوری خانگی در مسیر مشخص:

`adduser --home {{path/to/home}} {{username}}`

- ایجاد یک کاربر جدید با تنظیم پوسته (shell) مشخص به عنوان پوسته ورود:

`adduser --shell {{path/to/shell}} {{username}}`

- ایجاد یک کاربر جدید که به گروه مشخصی تعلق دارد:

`adduser --ingroup {{group}} {{username}}`
