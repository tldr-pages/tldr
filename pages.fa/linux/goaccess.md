# goaccess

> تحلیلگر متن‌باز و بلادرنگ گزارش‌های وب.
> اطلاعات بیشتر: <https://goaccess.io/man>.

- تحلیل یک یا چند فایل گزارش در حالت تعاملی:

`goaccess {{path/to/log1 path/to/log2 ...}}`

- استفاده از قالب گزارش مشخص یا قالب‌های ازپیش‌تعریف‌شده مانند «combined»:

`goaccess {{path/to/logfile}} --log-format={{format}}`

- تحلیل گزارش از ورودی استاندارد `stdin`:

`tail {{[-f|--follow]}} {{path/to/logfile}} | goaccess -`

- تحلیل گزارش و نوشتن آن در فایل HTML به‌صورت بلادرنگ:

`goaccess {{path/to/logfile}} {{[-o|--output]}} {{path/to/file.html}} --real-time-html`
