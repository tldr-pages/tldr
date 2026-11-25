# systemd-cryptsetup

> ایجاد یا حذف نگاشت‌های رمزگشایی‌شدهٔ حجم‌های رمزگذاری‌شده. معادل `cryptsetup open` و `cryptsetup close`.
> آرگومان‌های این دستور دقیقاً مانند یک خط در `/etc/crypttab` نوشته می‌شوند. systemd از آن برای باز کردن دستگاه‌ها هنگام راه‌اندازی استفاده می‌کند.
> همچنین ببینید: `cryptsetup`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-cryptsetup.html>.

- باز کردن حجم LUKS و ایجاد نگاشت رمزگشایی‌شده در `/dev/mapper/mapping_name`:

`systemd-cryptsetup attach {{mapping_name}} {{/dev/sdXY}}`

- باز کردن حجم LUKS با گزینه‌های اضافی و ایجاد نگاشت رمزگشایی‌شده در `/dev/mapper/mapping_name`:

`systemd-cryptsetup attach {{mapping_name}} {{/dev/sdXY}} none {{crypttab_options}}`

- باز کردن حجم LUKS با فایل کلید و ایجاد نگاشت رمزگشایی‌شده در `/dev/mapper/mapping_name`:

`systemd-cryptsetup attach {{mapping_name}} {{/dev/sdXY}} {{path/to/keyfile}} {{crypttab_options}}`

- حذف نگاشت موجود:

`systemd-cryptsetup detach {{mapping_name}}`
