# aa-audit

> تنظیم پروفایل‌های امنیتی AppArmor در حالت ممیزی.
> اطلاعات بیشتر: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-audit.8>.

- تنظیم یک پروفایل در حالت ممیزی:

`sudo aa-audit {{profile_name}}`

- تنظیم چند پروفایل در حالت ممیزی:

`sudo aa-audit {{profile1 profile2 ...}}`

- تنظیم یک پروفایل از دایرکتوری مشخص در حالت ممیزی:

`sudo aa-audit {{[-d|--dir]}} /{{path/to/profiles}} {{profile_name}}`

- اعمال اجباری حالت ممیزی حتی اگر قبلاً اعمال شده باشد:

`sudo aa-audit --force {{profile_name}}`

- تنظیم یک پروفایل در حالت ممیزی بدون بارگذاری مجدد آن:

`sudo aa-audit --no-reload {{profile_name}}`

- حذف حالت ممیزی از یک پروفایل:

`sudo aa-audit {{[-r|--remove]}} {{profile_name}}`

- نمایش راهنما:

`aa-audit {{[-h|--help]}}`
