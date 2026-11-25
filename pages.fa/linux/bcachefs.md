# bcachefs

> مدیریت سیستم‌های فایل و دستگاه‌های `bcachefs`.
> برخی زیردستورها مانند `device` مستندات استفادهٔ جداگانه دارند.
> اطلاعات بیشتر: <https://bcachefs-docs.readthedocs.io/en/latest/index.html>.

- قالب‌بندی یک پارتیشن با `bcachefs`:

`sudo bcachefs format {{path/to/partition}}`

- سوار کردن یک سیستم فایل `bcachefs`:

`sudo bcachefs mount {{path/to/partition}} {{path/to/mount_point}}`

- ایجاد یک سیستم فایل RAID 0 که در آن SSD به‌عنوان حافظهٔ نهان و HDD به‌عنوان ذخیره‌سازی بلندمدت عمل می‌کند:

`sudo bcachefs format {{[-l|--label]}} {{ssd.ssd1}} {{path/to/ssd_partition}} {{[-l|--label]}} {{hdd.hdd1}} {{path/to/hdd_partition}} --replicas 1 --foreground_target {{ssd}} --promote_target {{ssd}} --background_target {{hdd}}`

- سوار کردن یک سیستم فایل چنددستگاهی:

`sudo bcachefs mount {{path/to/partition1}}:{{path/to/partition2}} {{path/to/mount_point}}`

- نمایش میزان استفاده از دیسک:

`bcachefs fs usage {{[-h|--human-readable]}} {{path/to/mount_point}}`

- تنظیم تعداد نسخه‌های تکراری پس از قالب‌بندی و سوار کردن:

`sudo bcachefs set-fs-option --metadata_replicas {{2}} --data_replicas {{2}} {{path/to/partition}}`

- وادار کردن `bcachefs` به اطمینان از تکثیر همهٔ فایل‌ها:

`sudo bcachefs data rereplicate {{path/to/mount_point}}`

- ایجاد یک عکس لحظه‌ای از یک دایرکتوری مشخص:

`bcachefs subvolume snapshot {{path/to/directory}} {{path/to/snapshot}}`
