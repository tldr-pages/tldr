# lftp

> برنامهٔ پیشرفتهٔ انتقال فایل.
> اطلاعات بیشتر: <https://lftp.yar.ru/lftp-man.html>.

- اتصال به سرور FTP:

`lftp {{[-u|--user]}} {{username}} {{ftp.example.com}}`

- [تعاملی] بارگیری چند فایل (عبارت `glob`):

`mget {{path/to/*.png}}`

- [تعاملی] بارگذاری چند فایل (عبارت `glob`):

`mput {{path/to/*.zip}}`

- [تعاملی] حذف چند فایل در سرور راه دور:

`mrm {{path/to/*.txt}}`

- [تعاملی] تغییر نام فایل در سرور راه دور:

`mv {{original_filename}} {{new_filename}}`

- [تعاملی] بارگیری یا به‌روزرسانی کل دایرکتوری:

`mirror {{path/to/remote_directory}} {{path/to/local_output_directory}}`

- [تعاملی] بارگذاری یا به‌روزرسانی کل دایرکتوری:

`mirror {{[-R|--reverse]}} {{path/to/local_directory}} {{path/to/remote_output_directory}}`
