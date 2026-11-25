# pvremove

> حذف برچسب‌های LVM از حجم‌های فیزیکی.
> اطلاعات بیشتر: <https://manned.org/pvremove>.

- حذف برچسب LVM از حجم فیزیکی:

`sudo pvremove {{/dev/sdXY}}`

- نمایش خروجی مفصل حین عملیات:

`sudo pvremove {{[-v|--verbose]}} {{/dev/sdXY}}`

- حذف برچسب LVM بدون درخواست تأیید:

`sudo pvremove {{[-y|--yes]}} {{/dev/sdXY}}`

- حذف اجباری برچسب LVM:

`sudo pvremove {{[-f|--force]}} {{/dev/sdXY}}`

- نمایش خروجی در قالب JSON:

`sudo pvremove --reportformat json {{/dev/sdXY}}`
