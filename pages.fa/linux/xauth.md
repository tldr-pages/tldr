# xauth

> ویرایش و نمایش اطلاعات مجوز مورد استفاده برای اتصال به سرور X.
> اطلاعات بیشتر: <https://manned.org/xauth>.

- شروع حالت تعاملی با فایل مجوز مشخص (پیش‌فرض `~/.Xauthority`):

`xauth -f {{path/to/file}}`

- نمایش اطلاعات فایل مجوز:

`xauth info`

- نمایش مدخل‌های مجوز همهٔ نمایشگرها:

`xauth list`

- افزودن مجوز برای نمایشگر مشخص:

`xauth add {{display_name}} {{protocol_name}} {{key}}`

- حذف مجوز نمایشگر مشخص:

`xauth remove {{display_name}}`

- چاپ مدخل مجوز نمایشگر فعلی در `stdout`:

`xauth extract - $DISPLAY`

- ادغام مدخل‌های مجوز فایل مشخص در پایگاه دادهٔ مجوز:

`cat {{path/to/file}} | xauth merge -`

- نمایش راهنما:

`xauth --help`
