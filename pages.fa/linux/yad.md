# yad

> نمایش جعبه‌های گفت‌وگوی GTK+ از اسکریپت‌های پوسته.
> همچنین : `zenity`.
> اطلاعات بیشتر: <https://manned.org/yad>.

- نمایش محتوای فایل در جعبهٔ اطلاعات متنی:

`yad --text-info --filename {{path/to/file}}`

- باز کردن جعبهٔ ورود متن و بازگرداندن ورودی به `stdout`:

`yad --entry --text "{{message}}"`

- باز کردن انتخابگر فایل با عنوان مشخص:

`yad --file --title "{{title_message}}"`

- باز کردن جعبهٔ انتخاب تاریخ با عنوان مشخص:

`yad --calendar --title "{{title_message}}"`

- نمایش جعبهٔ فهرست با چند ستون و داده:

`yad --list --column "{{col1}}" --column "{{col2}}" {{col1_row1 col2_row1 col1_row2 col2_row2 ...}}`

- باز کردن نوار پیشرفت تپنده که در ۱۰۰٪ خودکار بسته می‌شود:

`{{command}} | yad --progress --pulsate --auto-close --text "{{message}}"`
