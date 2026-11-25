# sfdisk

> نمایش یا تغییر جدول پارتیشن دیسک.
> اطلاعات بیشتر: <https://manned.org/sfdisk>.

- پشتیبان‌گیری از چیدمان پارتیشن در فایل:

`sudo sfdisk {{[-d|--dump]}} {{/dev/sdX}} >{{path/to/file.dump}}`

- بازیابی چیدمان پارتیشن:

`sudo sfdisk <{{path/to/file.dump}} {{/dev/sdX}}`

- تنظیم نوع پارتیشن:

`sudo sfdisk --part-type {{/dev/sdX}} {{partition_number}} {{swap}}`

- حذف پارتیشن:

`sudo sfdisk --delete {{/dev/sdX}} {{partition_number}}`

- نمایش راهنما:

`sfdisk {{[-h|--help]}}`
