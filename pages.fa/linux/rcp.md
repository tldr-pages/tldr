# rcp

> کپی فایل‌ها بین سیستم‌های محلی و راه دور.
> رفتار دستور `cp` را تقلید می‌کند اما میان دستگاه‌های مختلف کار می‌کند.
> اطلاعات بیشتر: <https://www.gnu.org/software/inetutils/manual/inetutils.html#rcp-invocation>.

- کپی فایل به میزبان راه دور:

`rcp {{path/to/local_file}} {{username}}@{{remote_host}}:/{{path/to/destination}}/`

- کپی بازگشتی دایرکتوری:

`rcp {{[-r|--recursive]}} {{path/to/local_directory}} {{username}}@{{remote_host}}:/{{path/to/destination}}/`

- حفظ ویژگی‌های فایل:

`rcp {{[-p|--preserve]}} {{path/to/local_file}} {{username}}@{{remote_host}}:/{{path/to/destination}}/`

- کپی اجباری بدون تأیید:

`rcp {{[-f|--from]}} {{path/to/local_file}} {{username}}@{{remote_host}}:/{{path/to/destination}}/`
