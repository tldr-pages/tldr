# findmnt

> یافتن سیستم فایل.
> اطلاعات بیشتر: <https://manned.org/findmnt>.

- فهرست کردن همهٔ سیستم‌های فایل سوارشده:

`findmnt`

- جست‌وجوی یک دستگاه:

`findmnt {{/dev/sdb1}}`

- جست‌وجوی یک نقطهٔ اتصال:

`findmnt {{/}}`

- یافتن سیستم‌های فایل از نوع مشخص:

`findmnt {{[-t|--types]}} {{ext4,virtiofs,btrfs,...}}`

- یافتن سیستم‌های فایل با برچسب مشخص:

`findmnt LABEL={{BigStorage}}`

- بررسی مفصل محتوای جدول اتصال و اعتبارسنجی `/etc/fstab`:

`findmnt {{[-x|--verify]}} --verbose`
