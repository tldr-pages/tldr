# isosize

> نمایش اندازهٔ فایل ISO.
> اطلاعات بیشتر: <https://manned.org/isosize>.

- نمایش اندازهٔ فایل ISO:

`isosize {{path/to/file.iso}}`

- نمایش تعداد و اندازهٔ بلوک‌های فایل ISO:

`isosize {{[-x|--sectors]}} {{path/to/file.iso}}`

- نمایش اندازهٔ فایل ISO تقسیم بر عدد مشخص (فقط زمانی قابل استفاده است که `--sectors` داده نشده باشد):

`isosize {{[-d|--divisor]}} {{number}} {{path/to/file.iso}}`
