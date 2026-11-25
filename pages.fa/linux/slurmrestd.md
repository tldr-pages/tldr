# slurmrestd

> رابط Slurm از طریق REST API.
> توجه: در دو حالت Inetd و Listen قابل استفاده است.
> اطلاعات بیشتر: <https://slurm.schedmd.com/slurmrestd.html>.

- تغییر شناسهٔ گروه (و حذف گروه‌های تکمیلی) پیش از پردازش درخواست‌های کارخواه:

`slurmrestd -g {{group_id}} {{host:port|unix:/path/to/socket}}`

- تعیین فهرست افزونه‌های احراز هویت جداشده با ویرگول برای بارگذاری:

`slurmrestd -a {{authentication_plugins}} {{host:port|unix:/path/to/socket}}`

- خواندن پیکربندی Slurm از فایل مشخص:

`slurmrestd -f {{path/to/file}}`

- تغییر شناسهٔ کاربر پیش از پردازش درخواست کارخواه:

`slurmrestd -u {{user_id}}`

- نمایش راهنما:

`slurmrestd -h`

- نمایش نسخه:

`slurmrestd -V`
