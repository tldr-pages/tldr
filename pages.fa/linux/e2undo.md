# e2undo

> بازپخش گزارش‌های بازگردانی برای یک سیستم فایل ext2/ext3/ext4.
> می‌توان از آن برای بازگرداندن عملیات ناموفق یک برنامهٔ e2fsprogs استفاده کرد.
> اطلاعات بیشتر: <https://manned.org/e2undo>.

- نمایش اطلاعات یک فایل بازگردانی مشخص:

`e2undo -h {{path/to/undo_file}} {{/dev/sdXN}}`

- شبیه‌سازی بازپخش فایل بازگردانی و نمایش بلوک‌های نامزد:

`e2undo -nv {{path/to/undo_file}} {{/dev/sdXN}}`

- انجام عملیات بازگردانی:

`e2undo {{path/to/undo_file}} {{/dev/sdXN}}`

- انجام عملیات بازگردانی و نمایش اطلاعات مفصل با `-v`:

`e2undo -v {{path/to/undo_file}} {{/dev/sdXN}}`

- نوشتن محتویات قدیمی بلوک در فایل بازگردانی پیش از بازنویسی بلوک سیستم فایل:

`e2undo -z {{path/to/file.e2undo}} {{path/to/undo_file}} {{/dev/sdXN}}`
