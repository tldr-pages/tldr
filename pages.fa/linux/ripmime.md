# ripmime

> استخراج پیوست‌ها از بستهٔ ایمیل رمزگذاری‌شده با MIME.
> اطلاعات بیشتر: <https://pldaniels.com/ripmime/>.

- استخراج محتویات فایل در دایرکتوری فعلی:

`ripmime -i {{path/to/file}}`

- استخراج محتویات فایل در دایرکتوری مشخص:

`ripmime -i {{path/to/file}} -d {{path/to/directory}}`

- استخراج محتویات فایل و چاپ خروجی مفصل:

`ripmime -i {{path/to/file}} -v`

- دریافت اطلاعات دقیق دربارهٔ کل فرایند رمزگشایی:

`ripmime -i {{path/to/file}} --debug`
