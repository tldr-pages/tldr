# pacini

> پرس‌وجوی فایل‌های پیکربندی به سبک pacman.
> اطلاعات بیشتر: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacini.pod>.

- نمایش فایل پیکربندی کامل تجزیه‌شده (پیش‌فرض: `stdin`):

`pacini {{path/to/file}}`

- فهرست کردن بخش‌های پیکربندی‌شده:

`pacini {{path/to/file}} --section-list`

- نمایش همیشگی نام دستورها حتی در صورت ارائهٔ فقط یک دستور:

`pacini {{path/to/file}} --verbose`

- نمایش دستورهای فهرست‌شده در بخش مشخص:

`pacini {{path/to/file}} --section {{section_name}}`

- نمایش راهنما:

`pacini --help`

- نمایش نسخه:

`pacini --version`
