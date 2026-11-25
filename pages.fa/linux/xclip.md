# xclip

> ابزار کار با کلیپ‌بورد X11، مشابه `xsel`.
> انتخاب‌های اولیه و ثانویهٔ X و همچنین کلیپ‌بورد سیستم (`<Ctrl c>`/`<Ctrl v>`) را مدیریت می‌کند.
> همچنین : `wl-copy`.
> اطلاعات بیشتر: <https://manned.org/xclip>.

- کپی خروجی دستور در ناحیهٔ انتخاب اولیهٔ X11 (کلیپ‌بورد):

`echo 123 | xclip`

- کپی خروجی دستور در ناحیهٔ انتخاب مشخص X11:

`echo 123 | xclip {{[-se|-selection]}} {{primary|secondary|clipboard}}`

- کپی خروجی دستور در کلیپ‌بورد سیستم با نمادگذاری کوتاه:

`echo 123 | xclip {{[-se|-selection]}} {{[c|clipboard]}}`

- کپی محتوای فایل در کلیپ‌بورد سیستم:

`xclip {{[-se|-selection]}} {{[c|clipboard]}} {{path/to/input_file.txt}}`

- کپی محتوای PNG در کلیپ‌بورد سیستم (در برنامه‌های دیگر به‌درستی قابل چسباندن است):

`xclip {{[-se|-selection]}} {{[c|clipboard]}} {{[-t|-target]}} image/png {{path/to/input_file.png}}`

- کپی ورودی کاربر در کنسول به کلیپ‌بورد سیستم:

`xclip {{[-i|-in]}}`

- چسباندن محتوای ناحیهٔ انتخاب اولیهٔ X11 در کنسول:

`xclip {{[-o|-out]}}`

- چسباندن محتوای کلیپ‌بورد سیستم در کنسول:

`xclip {{[-o|-out]}} {{[-se|-selection]}} {{[c|clipboard]}}`
