# chmem

> تغییر وضعیت بلوک‌های حافظه (آنلاین یا آفلاین) در یک سیستم لینوکسی.
> معمولاً در محیط‌های مجازی برای مدیریت افزودن یا حذف حافظه در حال کار استفاده می‌شود.
> اطلاعات بیشتر: <https://manned.org/chmem>.

- آفلاین کردن یک بلوک حافظه:

`sudo chmem {{[-b|--block]}} {{[-d|--disable]}} {{block_number}}`

- آنلاین کردن یک بلوک حافظه:

`sudo chmem {{[-b|--block]}} {{[-e|--enable]}} {{block_number}}`

- آفلاین کردن یک بازهٔ حافظه با استفاده از آدرس‌های شانزده‌شانزدهی:

`sudo chmem {{[-d|--disable]}} 0x{{start_address}}-0x{{end_address}}`

- آنلاین کردن یک بازهٔ حافظه با استفاده از آدرس‌های شانزده‌شانزدهی:

`sudo chmem {{[-e|--enable]}} 0x{{start_address}}-0x{{end_address}}`

- آنلاین کردن حافظه و اختصاص آن به یک ناحیهٔ مشخص (مانند Movable):

`sudo chmem {{[-e|--enable]}} 0x{{start_address}} {{[-z|--zone]}} {{Movable}}`

- نمایش راهنما:

`chmem {{[-h|--help]}}`
