# csvkit

> ابزاری برای کارکردن با فایل های CSV.
> همچنین ببینید: `csvclean`, `csvcut`, `csvformat`, `csvgrep`, `csvlook`, `csvpy`, `csvsort`, `csvstat`.
> اطلاعات بیشتر: <https://csvkit.readthedocs.io/en/0.9.1/cli.html>.

- اجرای یک دستور روی یک فایل CSV با جداکننده دلخواه:

`{{command}} -d {{delimiter}} {{path/to/file.csv}}`

- اجرای یک دستور روی یک فایل CSV با استفاده از tab به عنوان جداکننده:

`{{command}} -t {{path/to/file.csv}}`

- اجرای یک دستور روی فایل CSV با کاراکتر نقلی شخصی سازی شده:

`{{command}} -q {{quote_char}} {{path/to/file.csv}}`

- اجرای یک دستور روی یک فایل CSV بدون خط هدر:

`{{command}} -H {{path/to/file.csv}}`
