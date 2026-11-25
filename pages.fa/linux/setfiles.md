# setfiles

> تنظیم زمینه‌های امنیتی فایل SELinux بر اساس قوانین سیاست.
> مشابه `restorecon` است اما زمینه‌ها را از فایل file_contexts می‌خواند.
> همچنین ببینید: `restorecon`, `semanage fcontext`, `fixfiles`.
> اطلاعات بیشتر: <https://manned.org/setfiles>.

- تنظیم زمینه‌های فایل مطابق فایل سیاست پیش‌فرض:

`sudo setfiles /etc/selinux/targeted/contexts/files/file_contexts {{path/to/directory}}`

- تنظیم بازگشتی زمینه‌های فایل و نمایش تغییرات:

`sudo setfiles /etc/selinux/targeted/contexts/files/file_contexts {{path/to/directory}} {{[-v|--verbose]}}`

- پیش‌نمایش تغییرات بدون تغییر واقعی زمینه‌ها:

`sudo setfiles /etc/selinux/targeted/contexts/files/file_contexts {{path/to/directory}} {{[-n|--nochange]}}`

- تنظیم زمینه‌های فایل و بررسی آن‌ها:

`sudo setfiles /etc/selinux/targeted/contexts/files/file_contexts {{path/to/directory}} {{[-v|--verbose]}} {{[-F|--force]}}`

- استفاده از مسیر ریشهٔ مشخص برای تطبیق زمینه:

`sudo setfiles /etc/selinux/targeted/contexts/files/file_contexts {{path/to/new_directory}} {{[-r|--rootpath]}} {{path/to/old_directory}}`
