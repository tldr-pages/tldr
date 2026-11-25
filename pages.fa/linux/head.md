# head

> چاپ بخش ابتدایی فایل‌ها.
> همچنین : `tail`.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html>.

- نمایش ۱۰ خط نخست یک فایل:

`head {{path/to/file}}`

- نمایش ۱۰ خط نخست چند فایل:

`head {{path/to/file1 path/to/file2 ...}}`

- چاپ ۵ خط نخست یک فایل:

`head {{[-5|--lines 5]}} {{path/to/file}}`

- چاپ چند خط نخست یک فایل:

`head {{[-n|--lines]}} {{count}} {{path/to/file}}`

- چاپ چند بایت نخست یک فایل:

`head {{[-c|--bytes]}} {{count}} {{path/to/file}}`

- چاپ همهٔ فایل به‌جز چند خط آخر:

`head {{[-n|--lines]}} -{{count}} {{path/to/file}}`

- چاپ همهٔ فایل به‌جز چند بایت آخر:

`head {{[-c|--bytes]}} -{{count}} {{path/to/file}}`
