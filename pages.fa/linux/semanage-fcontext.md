# semanage fcontext

> مدیریت قوانین پایدار زمینهٔ امنیتی SELinux برای فایل‌ها و دایرکتوری‌ها.
> همچنین : `matchpathcon`, `secon`, `chcon`, `restorecon`.
> اطلاعات بیشتر: <https://manned.org/semanage-fcontext>.

- فهرست کردن همهٔ قوانین برچسب‌گذاری فایل:

`sudo semanage fcontext {{[-l|--list]}}`

- فهرست کردن همهٔ قوانین برچسب‌گذاری فایل تعریف‌شده توسط کاربر بدون سربرگ:

`sudo semanage fcontext {{[-lCn|--list --locallist --noheading]}}`

- افزودن قانون کاربری برای برچسب‌گذاری هر مسیر مطابق `regex` از نوع PCRE:

`sudo semanage fcontext {{[-a|--add]}} {{[-t|--type]}} {{samba_share_t}} '{{/mnt/share(/.*)?}}'`

- افزودن قانون کاربری برای ایجاد هم‌ارزی برچسب‌گذاری بین دو زیرمسیر:

`sudo semanage fcontext {{[-a|--add]}} {{[-e|--equal]}} /{{path/to/ref}} /{{path/to/target}}`

- حذف قانون کاربری با استفاده از `regex` نوع PCRE آن:

`sudo semanage fcontext {{[-d|--delete]}} '{{/mnt/share(/.*)?}}'`

- برچسب‌گذاری مجدد بازگشتی دایرکتوری با اعمال قوانین جدید:

`restorecon -Rv {{path/to/directory}}`
