# aa-enforce

> تنظیم یک پروفایل AppArmor در حالت اعمال اجباری (enforce).
> همچنین : `aa-complain`, `aa-disable`, `aa-status`.
> اطلاعات بیشتر: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>.

- فعال کردن پروفایل:

`sudo aa-enforce {{[-d|--dir]}} {{path/to/profile}}`

- فعال کردن پروفایل‌ها:

`sudo aa-enforce {{path/to/profile1 path/to/profile2 ...}}`
