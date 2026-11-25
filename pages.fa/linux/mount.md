# mount

> دسترسی به کل فایل‌سیستم در یک دایرکتوری.
> همچنین ببینید: `udisksctl`.
> اطلاعات بیشتر: <https://manned.org/mount.8>.

- نمایش همهٔ فایل‌سیستم‌های سوارشده:

`mount`

- سوار کردن دستگاه در دایرکتوری:

`mount {{path/to/device_file}} {{path/to/target_directory}}`

- ایجاد دایرکتوری مشخص در صورت نبود و سوار کردن دستگاه در آن:

`mount {{[-m|--mkdir]}} {{path/to/device_file}} {{path/to/target_directory}}`

- سوار کردن دستگاه در دایرکتوری برای کاربر مشخص:

`mount {{[-o|--options]}} uid={{user_id}},gid={{group_id}} {{path/to/device_file}} {{path/to/target_directory}}`

- سوار کردن دستگاه CD-ROM (با نوع فایل ISO9660) در `/cdrom` به‌صورت فقط‌خواندنی:

`mount {{[-t|--types]}} iso9660 {{[-o|--options]}} ro {{/dev/cdrom}} /cdrom`

- سوار کردن همهٔ فایل‌سیستم‌های تعریف‌شده در `/etc/fstab`:

`mount {{[-a|--all]}}`

- سوار کردن فایل‌سیستم مشخص توصیف‌شده در `/etc/fstab` (مثلاً `/dev/sda1 /path/to/mount_point ext2 defaults 0 2`):

`mount {{path/to/mount_point}}`

- سوار کردن دایرکتوری در دایرکتوری دیگر:

`mount {{[-B|--bind]}} {{path/to/old_directory}} {{path/to/new_directory}}`
