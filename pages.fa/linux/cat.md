# cat

> چاپ و به‌هم‌پیوستن فایل‌ها.
> همچنین ببینید: `bat`.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html>.

- چاپ محتویات یک فایل در خروجی استاندارد `stdout`:

`cat {{path/to/file}}`

- به‌هم‌پیوستن چند فایل در یک فایل خروجی:

`cat {{path/to/file1 path/to/file2 ...}} >{{path/to/output_file}}`

- افزودن چند فایل به انتهای یک فایل خروجی:

`cat {{path/to/file1 path/to/file2 ...}} >>{{path/to/output_file}}`

- نوشتن تعاملی در یک فایل:

`cat >{{path/to/file}}`

- شماره‌گذاری همهٔ خطوط خروجی:

`cat {{[-n|--number]}} {{path/to/file}}`

- نمایش همهٔ نویسه‌ها، از جمله تب‌ها، پایان خط‌ها و نویسه‌های غیرقابل چاپ:

`cat {{[-A|--show-all]}} {{path/to/file}}`

- حذف خط‌های خالی تکراری:

`cat {{[-s|--squeeze-blank]}} {{path/to/file}}`

- انتقال محتویات فایل به برنامه‌ای دیگر از طریق ورودی استاندارد `stdin`:

`cat {{path/to/file}} | {{program}}`
