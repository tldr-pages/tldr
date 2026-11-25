# gphoto2

> کنترل دوربین‌های دیجیتال از خط فرمان.
> اطلاعات بیشتر: <http://www.gphoto.org/doc/manual/ref-gphoto2-cli.html>.

- فهرست کردن دوربین‌های متصل:

`gphoto2 --auto-detect`

- فهرست کردن فایل‌های دوربین:

`gphoto2 {{[-L|--list-files]}}`

- دانلود همهٔ تصاویر:

`gphoto2 {{[-P|--get-all-files]}}`

- دانلود فقط تصاویر جدید و رد کردن موارد موجود:

`gphoto2 {{[-P|--get-all-files]}} --new`

- دانلود فایل‌های ۱ تا ۵:

`gphoto2 {{[-p|--get-file]}} 1-5`

- حذف همهٔ فایل‌های دوربین:

`gphoto2 {{[-D|--delete-all-files]}}`

- گرفتن تصویر و دانلود آن:

`gphoto2 --capture-image-and-download`

- نمایش اطلاعات دوربین:

`gphoto2 --summary`
