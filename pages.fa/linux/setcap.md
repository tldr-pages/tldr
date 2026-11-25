# setcap

> تنظیم قابلیت‌های فایل مشخص.
> همچنین ببینید: `getcap`.
> اطلاعات بیشتر: <https://manned.org/setcap>.

- تنظیم قابلیت `cap_net_raw` (برای استفاده از سوکت‌های RAW و PACKET) برای فایل مشخص:

`setcap 'cap_net_raw' {{path/to/file}}`

- تنظیم چند قابلیت روی فایل (`ep` پس از قابلیت به معنی «مجاز و مؤثر» است):

`setcap '{{cap_dac_read_search,cap_sys_tty_config+ep}}' {{path/to/file}}`

- حذف همهٔ قابلیت‌ها از فایل:

`setcap -r {{path/to/file}}`

- بررسی ارتباط فعلی قابلیت‌های مشخص با فایل مشخص:

`setcap -v '{{cap_net_raw}}' {{path/to/file}}`

- تنظیم قابلیت فایل برای استفاده فقط در فضای نام کاربر با شناسهٔ مالک root مشخص:

`setcap -n {{root_uid}} '{{cap_net_admin}}' {{path/to/file}}`
