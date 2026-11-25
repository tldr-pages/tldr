# unsquashfs

> خارج کردن از حالت فشرده، استخراج و فهرست کردن فایل‌ها در فایل‌سیستم‌های squashfs.
> اطلاعات بیشتر: <https://manned.org/unsquashfs>.

- استخراج فایل‌سیستم squashfs در `squashfs-root` در دایرکتوری کاری فعلی:

`unsquashfs {{filesystem.squashfs}}`

- استخراج فایل‌سیستم squashfs در دایرکتوری مشخص:

`unsquashfs {{[-d|-dest]}} {{path/to/directory}} {{filesystem.squashfs}}`

- نمایش نام فایل‌ها هنگام استخراج:

`unsquashfs {{[-i|-info]}} {{filesystem.squashfs}}`

- نمایش نام فایل‌ها و ویژگی‌های آن‌ها هنگام استخراج:

`unsquashfs {{[-li|-linfo]}} {{filesystem.squashfs}}`

- فهرست کردن فایل‌های داخل فایل‌سیستم squashfs (بدون استخراج):

`unsquashfs {{[-l|-ls]}} {{filesystem.squashfs}}`

- فهرست کردن فایل‌ها و ویژگی‌های آن‌ها داخل فایل‌سیستم squashfs (بدون استخراج):

`unsquashfs {{[-ll|-lls]}} {{filesystem.squashfs}}`
