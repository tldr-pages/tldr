# qtile

> مدیر پنجرهٔ کاشی‌وار کامل و قابل تغییر که با Python نوشته و پیکربندی شده است.
> اطلاعات بیشتر: <https://docs.qtile.org/en/latest/manual/commands/shell/index.html>.

- شروع مدیر پنجره در صورت اجرا نبودن (بهتر است از `.xsession` یا مشابه اجرا شود):

`qtile start`

- بررسی خطاهای کامپایل فایل پیکربندی (محل پیش‌فرض `~/.config/qtile/config.py`):

`qtile check`

- نمایش اطلاعات فعلی مصرف منابع:

`qtile top --force`

- باز کردن برنامهٔ `xterm` به‌صورت پنجرهٔ شناور در گروهی به نام `test-group`:

`qtile run-cmd --group {{test_group}} --float {{xterm}}`

- راه‌اندازی مجدد مدیر پنجره:

`qtile cmd-obj --object cmd --function restart`
