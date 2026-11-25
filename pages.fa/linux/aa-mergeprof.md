# aa-mergeprof

> ادغام فایل‌های پروفایل امنیتی AppArmor در دایرکتوری پروفایل‌ها.
> اطلاعات بیشتر: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-mergeprof.8>.

- ادغام یک یا چند فایل پروفایل در دایرکتوری پیش‌فرض پروفایل‌ها:

`sudo aa-mergeprof {{file1 file2 ...}}`

- ادغام فایل‌های پروفایل در یک دایرکتوری مشخص:

`sudo aa-mergeprof {{[-d|--dir]}} /{{path/to/profiles}} {{file1 file2 ...}}`

- نمایش راهنما:

`aa-mergeprof {{[-h|--help]}}`
