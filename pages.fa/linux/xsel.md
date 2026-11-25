# xsel

> ابزار کار با انتخاب و کلیپ‌بورد X11.
> اطلاعات بیشتر: <https://manned.org/xsel>.

- استفاده از خروجی دستور به‌عنوان ورودی کلیپ‌بورد (معادل `<Ctrl c>`):

`echo 123 | xsel {{[-ib|--input --clipboard]}}`

- استفاده از محتوای فایل به‌عنوان ورودی کلیپ‌بورد:

`cat {{path/to/file}} | xsel {{[-ib|--input --clipboard]}}`

- خروجی محتوای کلیپ‌بورد به ترمینال (معادل `<Ctrl v>`):

`xsel {{[-ob|--output --clipboard]}}`

- خروجی محتوای کلیپ‌بورد به فایل:

`xsel {{[-ob|--output --clipboard]}} >{{path/to/file}}`

- پاک کردن کلیپ‌بورد:

`xsel {{[-cb|--clear --clipboard]}}`

- خروجی محتوای انتخاب اولیهٔ X11 به ترمینال (معادل کلیک میانی ماوس `<MiddleClick>`):

`xsel {{[-op|--output --primary]}}`
