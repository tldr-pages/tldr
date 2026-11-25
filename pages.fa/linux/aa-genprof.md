# aa-genprof

> تولید پروفایل‌های امنیتی AppArmor با نظارت بر رفتار برنامه.
> اطلاعات بیشتر: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-genprof.8>.

- شروع تولید یک پروفایل برای برنامه:

`sudo aa-genprof {{path/to/program}}`

- مشخص کردن یک دایرکتوری دلخواه برای پروفایل‌ها:

`sudo aa-genprof {{[-d|--dir]}} /{{path/to/profiles}} {{path/to/program}}`

- مشخص کردن یک فایل گزارش دلخواه برای پروفایل‌سازی:

`sudo aa-genprof {{[-f|--file]}} /{{path/to/logfile}} {{path/to/program}}`

- نمایش راهنما:

`aa-genprof {{[-h|--help]}}`
