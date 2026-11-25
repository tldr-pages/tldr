# rdesktop

> کارخواه پروتکل دسکتاپ راه دور.
> می‌توان از آن برای اتصال به رایانهٔ راه دور با پروتکل RDP استفاده کرد.
> اطلاعات بیشتر: <https://manned.org/rdesktop>.

- اتصال به رایانهٔ راه دور (پورت پیش‌فرض ۳۳۸۹):

`rdesktop -u {{username}} -p {{password}} {{host:port}}`

- اتصال به رایانهٔ راه دور به‌عنوان `Administrator` با رمز عبور مشخص:

`rdesktop -u Administrator -p passwd123 192.168.1.111:3389`

- اتصال به رایانهٔ راه دور در حالت تمام‌صفحه (برای خروج `<Ctrl Alt Enter>` را فشار دهید):

`rdesktop -u {{username}} -p {{password}} -f {{host:port}}`

- استفاده از وضوح دلخواه (از حرف `x` بین اعداد استفاده کنید):

`rdesktop -u {{username}} -p {{password}} -g {{1366}}x{{768}} {{host:port}}`

- اتصال به رایانهٔ راه دور با کاربر دامنه:

`rdesktop -u {{username}} -p {{password}} -d {{domainname}} {{host:port}}`

- استفاده از رنگ ۱۶ بیتی (برای سرعت بیشتر):

`rdesktop -u {{username}} -p {{password}} -a 16 {{host:port}}`
