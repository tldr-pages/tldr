# systemd-sysusers

> ایجاد کاربران و گروه‌های سیستمی.
> اگر فایل پیکربندی مشخص نشود، از فایل‌های دایرکتوری‌های `sysusers.d` استفاده می‌شود.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-sysusers.html>.

- ایجاد کاربران و گروه‌ها از فایل پیکربندی مشخص:

`systemd-sysusers {{path/to/file}}`

- شبیه‌سازی پردازش فایل‌های پیکربندی و چاپ عملیات احتمالی:

`systemd-sysusers --dry-run {{path/to/file}}`

- چاپ محتویات همهٔ فایل‌های پیکربندی (نام هر فایل پیش از آن به‌صورت توضیح چاپ می‌شود):

`systemd-sysusers --cat-config`

- ایجاد کاربران بر اساس فایل‌های فهرست‌شده در دستور قبلی:

`systemd-sysusers`
