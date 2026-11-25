# homectl

> ایجاد، حذف، تغییر یا بررسی دایرکتوری‌های خانگی با سرویس systemd-homed.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/homectl.html>.

- فهرست کردن حساب‌های کاربری و دایرکتوری‌های خانگی مرتبط:

`homectl list`

- ایجاد حساب کاربری و دایرکتوری خانگی مرتبط:

`sudo homectl create {{username}}`

- حذف کاربر مشخص و دایرکتوری خانگی مرتبط:

`sudo homectl remove {{username}}`

- تغییر رمز عبور کاربر مشخص:

`sudo homectl passwd {{username}}`

- اجرای پوسته یا دستور با دسترسی به دایرکتوری خانگی مشخص:

`sudo homectl with {{username}} -- {{command}} {{command_arguments}}`

- قفل یا باز کردن قفل دایرکتوری خانگی مشخص:

`sudo homectl {{lock|unlock}} {{username}}`

- تغییر فضای دیسک اختصاص‌یافته به دایرکتوری خانگی مشخص به ۱۰۰ GiB:

`sudo homectl resize {{username}} {{100G}}`

- نمایش راهنما:

`homectl {{[-h|--help]}}`
