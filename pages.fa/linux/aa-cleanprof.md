# aa-cleanprof

> پاکسازی پروفایل‌های امنیتی AppArmor با حذف قواعد استفاده‌نشده.
> اطلاعات بیشتر: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-cleanprof.8>.

- پاکسازی یک پروفایل برای حذف قواعد استفاده‌نشده:

`sudo aa-cleanprof {{profile_name}}`

- پاکسازی چند پروفایل به‌صورت هم‌زمان:

`sudo aa-cleanprof {{profile1 profile2 ...}}`

- مشخص کردن دایرکتوری حاوی پروفایل‌ها:

`sudo aa-cleanprof {{[-d|--dir]}} /{{path/to/profiles}} {{profile_name}}`

- اجرای بی‌صدا و بدون درخواست تأیید:

`sudo aa-cleanprof {{[-s|--silent]}} {{profile_name}}`

- جلوگیری از بارگذاری مجدد پروفایل پس از پاکسازی:

`sudo aa-cleanprof --no-reload {{profile_name}}`

- نمایش راهنما:

`aa-cleanprof {{[-h|--help]}}`
