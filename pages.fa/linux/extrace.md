# extrace

> ردیابی فراخوانی‌های exec().
> اطلاعات بیشتر: <https://github.com/leahneukirchen/extrace>.

- ردیابی همهٔ اجراهای برنامه در سیستم:

`sudo extrace`

- اجرای یک دستور و ردیابی فقط فرزندان آن:

`sudo extrace {{command}}`

- چاپ دایرکتوری کاری فعلی هر فرایند با `-d`:

`sudo extrace -d`

- تعیین مسیر کامل هر فایل اجرایی:

`sudo extrace -l`

- نمایش کاربر اجراکنندهٔ هر فرایند با `-u`:

`sudo extrace -u`
