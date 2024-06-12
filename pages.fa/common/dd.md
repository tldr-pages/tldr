# dd

> تبدیل و کپی یک فایل.
> اطلاعات بیشتر: <https://manned.org/man/dd.1p>.

- یک حافظه قابل حمل با قابلیت بوت شدن میسازد، برای مثال `archlinux-xxx.iso` :

`dd if={{path/to/file.iso}} of={{/dev/usb_drive}}`

- محتویات یک درایو را در مکانی دیگر با بلوک های 4 مگابایتی کپی و همچنین از خطاها صرف نظر میکند:

`dd bs=4194304 conv=noerror if={{/dev/source_drive}} of={{/dev/dest_drive}}`

- یک فایل ۱۰۰ بایتی تصادفی با استفاده از درایور تصادفی هسته بسازید:

`dd if=/dev/urandom of={{path/to/random_file}} bs=100 count={{1}}`

- عملکرد نوشتن دیسک را بسنجید:

`dd if=/dev/zero of={{path/to/file_1GB}} bs={{1024}} count={{1000000}}`

- یک پشتیبان از سیستم را در یک فایل IMG میسازد :

`dd if={{/dev/drive_device}} of={{path/to/file.img}}`

- یک درایو را از یک فایل IMG بازیابی کنید:

`dd if={{path/to/file.img}} of={{/dev/drive_device}}`
