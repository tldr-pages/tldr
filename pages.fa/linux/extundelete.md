# extundelete

> بازیابی فایل‌های حذف‌شده از پارتیشن‌های ext3 یا ext4 با تحلیل ژورنال.
> همچنین : `date`, `umount`.
> اطلاعات بیشتر: <https://extundelete.sourceforge.net/options.html>.

- بازیابی همهٔ فایل‌های حذف‌شده در پارتیشن `N` از دستگاه `X`:

`sudo extundelete {{/dev/sdXN}} --restore-all`

- بازیابی فایل از مسیری نسبت به ریشه (مسیر را با `/` شروع نکنید):

`extundelete {{/dev/sdXN}} --restore-file {{path/to/file}}`

- بازیابی دایرکتوری از مسیری نسبت به ریشه (مسیر را با `/` شروع نکنید):

`extundelete {{/dev/sdXN}} --restore-directory {{path/to/directory}}`

- بازیابی همهٔ فایل‌های حذف‌شده پس از اول ژانویهٔ ۲۰۲۰ (به وقت یونیکس):

`extundelete {{/dev/sdXN}} --restore-all --after {{1577840400}}`
