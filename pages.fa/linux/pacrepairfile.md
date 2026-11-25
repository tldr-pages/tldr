# pacrepairfile

> بازنشانی ویژگی‌های فایل‌های مدیریت‌شده توسط alpm.
> اطلاعات بیشتر: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacrepairfile.pod>.

- جست‌وجوی بسته و بازنشانی ویژگی‌های فایل:

`pacrepairfile {{path/to/file}} --package`

- بازنشانی فایل در حالت کم‌صدا:

`pacrepairfile {{package_name}} --quiet --package`

- بازنشانی ویژگی‌های مشخص فایل (حالت، UID مالک، GID گروه یا زمان تغییر):

`pacrepairfile {{package_name}} --{{mode|gid|mtime|uid}} --package`

- نمایش راهنما:

`pacrepairfile --help`

- نمایش نسخه:

`pacrepairfile --version`
