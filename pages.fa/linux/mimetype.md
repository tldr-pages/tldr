# mimetype

> تشخیص خودکار نوع MIME فایل.
> اطلاعات بیشتر: <https://manned.org/mimetype>.

- چاپ نوع MIME فایل مشخص:

`mimetype {{path/to/file}}`

- نمایش فقط نوع MIME و نه نام فایل:

`mimetype --brief {{path/to/file}}`

- نمایش توضیح نوع MIME:

`mimetype --describe {{path/to/file}}`

- تشخیص نوع MIME ورودی `stdin` (نام فایل را بررسی نمی‌کند):

`{{command}} | mimetype --stdin`

- نمایش اطلاعات اشکال‌زدایی دربارهٔ نحوهٔ تشخیص نوع MIME:

`mimetype --debug {{path/to/file}}`

- نمایش همهٔ انواع MIME ممکن فایل مشخص به ترتیب اطمینان:

`mimetype --all {{path/to/file}}`

- تعیین صریح کد دوحرفی زبان خروجی:

`mimetype --language {{path/to/file}}`
