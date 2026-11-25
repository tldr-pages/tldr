# aa-disable

> غیرفعال کردن سیاست‌های امنیتی AppArmor.
> همچنین ببینید: `aa-complain`, `aa-enforce`, `aa-status`.
> اطلاعات بیشتر: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- غیرفعال کردن پروفایل:

`sudo aa-disable {{path/to/profile1 path/to/profile2 ...}}`

- غیرفعال کردن پروفایل‌های یک دایرکتوری (به‌صورت پیش‌فرض `/etc/apparmor.d`):

`sudo aa-disable --dir {{path/to/profiles}}`
