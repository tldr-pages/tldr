# aa-logprof

> به‌روزرسانی تعاملی پروفایل‌های امنیتی AppArmor بر اساس تخلف‌های ثبت‌شده.
> اطلاعات بیشتر: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-logprof.8>.

- بررسی و به‌روزرسانی تعاملی پروفایل‌ها بر اساس گزارش‌های سیستم:

`sudo aa-logprof`

- استفاده از یک دایرکتوری مشخص برای پروفایل‌های AppArmor:

`sudo aa-logprof {{[-d|--dir]}} /{{path/to/profiles}}`

- استفاده از یک فایل گزارش مشخص به جای فایل پیش‌فرض:

`sudo aa-logprof {{[-f|--file]}} /{{path/to/logfile}}`

- نادیده گرفتن تمام ورودی‌های گزارش پیش از نشان مشخص‌شده:

`sudo aa-logprof {{[-m|--logmark]}} "{{log_marker_text}}"`

- نمایش راهنما:

`aa-logprof {{[-h|--help]}}`
