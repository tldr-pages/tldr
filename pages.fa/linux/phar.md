# phar

> ایجاد، به‌روزرسانی یا استخراج بایگانی‌های PHP (PHAR).
> اطلاعات بیشتر: <https://manned.org/phar>.

- افزودن یک یا چند فایل یا دایرکتوری به فایل Phar:

`phar add -f {{path/to/phar_file}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- نمایش محتویات فایل Phar:

`phar list -f {{path/to/phar_file}}`

- حذف فایل یا دایرکتوری مشخص از فایل Phar:

`phar delete -f {{path/to/phar_file}} -e {{path/to/file_or_directory}}`

- فشرده یا از حالت فشرده خارج کردن فایل‌ها و دایرکتوری‌های فایل Phar:

`phar compress -f {{path/to/phar_file}} -c {{algorithm}}`

- دریافت اطلاعات فایل Phar:

`phar info -f {{path/to/phar_file}}`

- امضای فایل Phar با الگوریتم هش مشخص:

`phar sign -f {{path/to/phar_file}} -h {{algorithm}}`

- امضای فایل Phar با کلید خصوصی OpenSSL:

`phar sign -f {{path/to/phar_file}} -h openssl -y {{path/to/private_key}}`

- نمایش راهنما و الگوریتم‌های هش و فشرده‌سازی موجود:

`phar help`
