# systemd-firstboot

> مقداردهی اولیهٔ تنظیمات پایهٔ سیستم در نخستین راه‌اندازی یا پیش از آن.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-firstboot.html>.

- عمل روی دایرکتوری مشخص به‌جای دایرکتوری ریشهٔ سیستم میزبان:

`sudo systemd-firstboot --root {{path/to/root_directory}}`

- تنظیم چیدمان صفحه‌کلید سیستم:

`sudo systemd-firstboot --keymap {{keymap}}`

- تنظیم نام میزبان سیستم:

`sudo systemd-firstboot --hostname {{hostname}}`

- تنظیم رمز عبور کاربر root:

`sudo systemd-firstboot --root-password {{password}}`

- درخواست تعاملی تنظیم پایهٔ مشخص از کاربر:

`sudo systemd-firstboot --prompt {{setting}}`

- اجبار نوشتن پیکربندی حتی اگر فایل‌های مربوط از قبل وجود داشته باشند:

`sudo systemd-firstboot --force`

- حذف همهٔ فایل‌های موجود پیکربندی‌شده توسط `systemd-firstboot`:

`sudo systemd-firstboot --reset`

- حذف رمز عبور کاربر root سیستم:

`sudo systemd-firstboot --delete-root-password`
