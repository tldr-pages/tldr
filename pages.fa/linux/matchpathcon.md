# matchpathcon

> جست‌وجوی تنظیمات پایدار زمینهٔ امنیتی SELinux برای یک مسیر.
> همچنین ببینید: `semanage fcontext`, `secon`, `chcon`, `restorecon`.
> اطلاعات بیشتر: <https://manned.org/matchpathcon.8>.

- جست‌وجوی تنظیمات پایدار زمینهٔ امنیتی مسیر مطلق:

`matchpathcon /{{path/to/file}}`

- محدود کردن جست‌وجو به تنظیمات یک نوع فایل مشخص:

`matchpathcon -m {{file|dir|pipe|chr_file|blk_file|lnk_file|sock_file}} /{{path/to/file}}`

- بررسی تطابق زمینهٔ امنیتی پایدار و فعلی مسیر:

`matchpathcon -V /{{path/to/file}}`
