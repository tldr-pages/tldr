# xbps-remove

> ابزار XBPS برای حذف بسته‌ها.
> همچنین ببینید: `xbps`.
> اطلاعات بیشتر: <https://manned.org/xbps-remove>.

- حذف بسته:

`xbps-remove {{package}}`

- حذف بسته و وابستگی‌های آن:

`xbps-remove {{[-R|--recursive]}} {{package}}`

- حذف بسته‌های یتیم (نصب‌شده به‌عنوان وابستگی اما دیگر مورد نیاز هیچ بسته‌ای نیستند):

`xbps-remove {{[-o|--remove-orphans]}}`

- حذف بسته‌های منسوخ از حافظهٔ نهان:

`xbps-remove {{[-O|--clean-cache]}}`
