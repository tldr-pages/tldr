# mktemp

> ایجاد فایل یا دایرکتوری موقت.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/mktemp-invocation.html>.

- ایجاد فایل موقت خالی و چاپ مسیر مطلق آن:

`mktemp`

- استفاده از دایرکتوری دلخواه (پیش‌فرض `$TMPDIR` یا `/tmp` است):

`mktemp {{[-p |--tmpdir=]}}/{{path/to/temporary_directory}}`

- استفاده از الگوی مسیر دلخواه (`X`ها با نویسه‌های تصادفی الفبایی‌عددی جایگزین می‌شوند):

`mktemp {{/tmp/example.XXXXXXXX}}`

- استفاده از الگوی نام فایل دلخواه:

`mktemp -t {{example.XXXXXXXX}}`

- ایجاد فایل موقت خالی با پسوند مشخص و چاپ مسیر مطلق آن:

`mktemp --suffix {{.ext}}`

- ایجاد دایرکتوری موقت خالی و چاپ مسیر مطلق آن:

`mktemp {{[-d|--directory]}}`

- چاپ نام فایل یا دایرکتوری موقت بدون ایجاد واقعی آن:

`mktemp {{[-u|--dry-run]}}`
