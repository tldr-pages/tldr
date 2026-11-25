# restorecon

> بازیابی زمینهٔ امنیتی SELinux فایل‌ها و دایرکتوری‌ها مطابق قوانین پایدار.
> همچنین : `semanage fcontext`.
> اطلاعات بیشتر: <https://manned.org/restorecon>.

- مشاهدهٔ زمینهٔ امنیتی فعلی فایل یا دایرکتوری:

`ls {{[-dlZ|--directory -l --context]}} {{path/to/file_or_directory}}`

- بازیابی زمینهٔ امنیتی فایل یا دایرکتوری:

`restorecon {{path/to/file_or_directory}}`

- بازیابی بازگشتی زمینهٔ امنیتی دایرکتوری و نمایش همهٔ برچسب‌های تغییرکرده:

`restorecon -R -v {{path/to/directory}}`

- بازیابی بازگشتی زمینهٔ امنیتی دایرکتوری با همهٔ رشته‌های موجود و نمایش پیشرفت:

`restorecon -R -T {{0}} -p {{path/to/directory}}`

- پیش‌نمایش تغییرات برچسب بدون اعمال آن‌ها:

`restorecon -R -n -v {{path/to/directory}}`
