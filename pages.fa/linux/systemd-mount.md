# systemd-mount

> ایجاد و حذف نقاط اتصال یا اتصال خودکار موقت.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-mount.html>.

- سوار کردن فایل‌سیستم (تصویر یا دستگاه بلوکی) در `/run/media/system/LABEL` که LABEL برچسب فایل‌سیستم یا در صورت نبود برچسب نام دستگاه است:

`systemd-mount {{path/to/file_or_device}}`

- سوار کردن فایل‌سیستم (تصویر یا دستگاه بلوکی) در محل مشخص:

`systemd-mount {{path/to/file_or_device}} {{path/to/mount_point}}`

- فهرست کردن همهٔ دستگاه‌های بلوکی محلی شناخته‌شده با فایل‌سیستم قابل اتصال:

`systemd-mount --list`

- ایجاد نقطهٔ اتصال خودکار که فایل‌سیستم واقعی را هنگام نخستین دسترسی سوار می‌کند:

`systemd-mount --automount yes {{path/to/file_or_device}}`

- پیاده کردن یک یا چند دستگاه:

`systemd-mount {{[-u|--umount]}} {{path/to/mount_point_or_device1 path/to/mount_point_or_device2 ...}}`

- سوار کردن فایل‌سیستم (تصویر یا دستگاه بلوکی) با نوع فایل‌سیستم مشخص:

`systemd-mount {{[-t|--type]}} {{file_system_type}} {{path/to/file_or_device}} {{path/to/mount_point}}`

- سوار کردن فایل‌سیستم (تصویر یا دستگاه بلوکی) با گزینه‌های اتصال اضافی:

`systemd-mount {{[-o|--options]}} {{mount_options}} {{path/to/file_or_device}} {{path/to/mount_point}}`
