# vgremove

> حذف گروه‌های حجم در LVM.
> اطلاعات بیشتر: <https://manned.org/vgremove>.

- حذف گروه حجم با تأیید:

`sudo vgremove {{volume_group}}`

- حذف اجباری گروه حجم بدون تأیید:

`sudo vgremove {{[-f|--force]}} {{volume_group}}`

- تنظیم سطح اشکال‌زدایی به ۲ برای ثبت مفصل (برای افزایش سطح `--debug` را تا ۶ بار تکرار کنید):

`sudo vgremove {{[-d|--debug]}} {{[-d|--debug]}} {{volume_group}}`

- استفاده از تنظیم پیکربندی مشخص به‌جای پیش‌فرض‌ها:

`sudo vgremove --config '{{global/locking_type=1}}' {{volume_group}}`

- نمایش راهنما:

`vgremove {{[-h|--help]}}`
