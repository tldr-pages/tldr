# 7zr

> بایگانی کننده فایل با فشرده سازی بالا.
> مشابه `7z` منحصر به پشتیبانی از فایل های `.7z`.
> اطلاعات بیشتر: <https://manned.org/7zr>.

- بایگانی کردن یک فایل یا پوشه :

`7zr a {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- رمزگذاری یک بایگانی (همراه با نام فایل ها) موجود :

`7zr a {{path/to/encrypted.7z}} -p{{password}} -mhe={{on}} {{path/to/archive.7z}}`

- استخراج یک بایگانی با نگهداری ساختار پوشه اصلی :

`7zr x {{path/to/archive.7z}}`

- استخراج یک بایگانی به پوشه معین :

`7zr x {{path/to/archive.7z}} -o{{path/to/output}}`

- استخراج یک بایگانی به خروجی استاندارد `stdout` :

`7zr x {{path/to/archive.7z}} -so`

- فهرست نمودن محتویات یک بایگانی :

`7zr l {{path/to/archive.7z}}`
