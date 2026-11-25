# script

> ثبت همهٔ خروجی ترمینال در فایل typescript.
> اطلاعات بیشتر: <https://manned.org/script>.

- ثبت نشست جدید در فایلی به نام `typescript` در دایرکتوری فعلی:

`script`

- توقف ثبت:

`exit`

- ثبت نشست جدید در مسیر فایل دلخواه:

`script {{path/to/session.out}}`

- افزودن به فایل موجود:

`script {{[-a|--append]}} {{logfile.log}}`

- ثبت اطلاعات زمان‌بندی (داده‌ها به `stderr` خروجی داده می‌شوند):

`script {{[-t|--timing]}} 2>{{path/to/timing_file}}`

- نوشتن داده‌ها به‌محض وقوع:

`script {{[-f|--flush]}} {{path/to/file}}`

- اجرای بی‌صدا بدون پیام‌های شروع و پایان:

`script {{[-q|--quiet]}} {{logfile.log}}`

- نمایش راهنما:

`script {{[-h|--help]}}`
