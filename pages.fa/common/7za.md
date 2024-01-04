# 7za

> بایگانی کننده فایل با ضریب فشرده سازی بالا.
> مشابه `7z` با قابلیت پشتیبانی از انواع فایل کمتر ولی قابلیت پشتیبانی از چندین سیستم عامل.
> اطلاعات بیشتر: <https://manned.org/7za>.

- بایگانی یک فایل یا یک پوشه :

`7za a {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- رمزگذاری یک بایگانی (با نام فایل ها) موجود :

`7za a {{path/to/encrypted.7z}} -p{{password}} -mhe={{on}} {{path/to/archive.7z}}`

- استخراج یک بایگانی با نگهداری ساختار پوشه مبدا :

`7za x {{path/to/archive.7z}}`

- استخراج یک بایگانی به یک پوشه معین :

`7za x {{path/to/archive.7z}} -o{{path/to/output}}`

- استخراج یک بایگانی به خروجی استاندارد :

`7za x {{path/to/archive.7z}} -so`

- بایگانی با نوع فایل مشخص شده :

`7za a -t{{7z|bzip2|gzip|lzip|tar|...}} {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- فهرست کردن محتویات یک بایگانی :

`7za l {{path/to/archive.7z}}`
