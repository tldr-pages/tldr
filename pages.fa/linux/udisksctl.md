# udisksctl

> تعامل با `udisksd` برای پرس‌وجو و تغییر دستگاه‌های ذخیره‌سازی.
> همچنین ببینید: `mount`.
> اطلاعات بیشتر: <https://storaged.org/doc/udisks2-api/latest/udisksctl.1.html>.

- نمایش اطلاعات سطح بالا دربارهٔ درایوهای دیسک و دستگاه‌های بلوکی:

`udisksctl status`

- نمایش اطلاعات مفصل دستگاه:

`udisksctl info {{[-b|--block-device]}} {{/dev/sdX}}`

- نمایش اطلاعات مفصل پارتیشن دستگاه:

`udisksctl info {{[-b|--block-device]}} {{/dev/sdXN}}`

- سوار کردن پارتیشن دستگاه و چاپ نقطهٔ اتصال:

`udisksctl mount {{[-b|--block-device]}} {{/dev/sdXN}}`

- پیاده کردن پارتیشن دستگاه:

`udisksctl unmount {{[-b|--block-device]}} {{/dev/sdXN}}`

- خاموش کردن دستگاه برای جداسازی امن:

`udisksctl power-off {{[-b|--block-device]}} {{/dev/sdX}}`

- پایش سرویس برای رویدادها:

`udisksctl monitor`
