# aa-complain

> تنظیم یک سیاست AppArmor در حالت گزارش تخلف (complain).
> همچنین ببینید: `aa-disable`, `aa-enforce`, `aa-status`.
> اطلاعات بیشتر: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-complain.8>.

- تنظیم سیاست در حالت گزارش تخلف:

`sudo aa-complain {{path/to/profile1 path/to/profile2 ...}}`

- تنظیم سیاست‌ها در حالت گزارش تخلف:

`sudo aa-complain {{[-d|--dir]}} {{path/to/profiles}}`
