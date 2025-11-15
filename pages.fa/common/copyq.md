# copyq

> مدیریت کلیپ بورد با قابلیت های پیشرفته.
> اطلاعات بیشتر: <https://copyq.readthedocs.io/en/latest/command-line.html>.

- اجرای کپی کیو برای ذخیره تاریخچه کلیپ بورد:

`copyq`

- نمایش محتوای کنونی کلیپ بورد:

`copyq clipboard`

- وارد کردن متن خام به تاریخچه کلیپ بورد:

`copyq add -- {{text1}} {{text2}} {{text3}}`

- وارد کردن متن شامل رشته های فاصله انداز مانند (\n, \t) در تاریخچه کلیپ بورد:

`copyq add {{firstline\nsecondline}}`

- چاپ محتوای سه مورد اول در تاریخچه کلیپ بورد:

`copyq read 0 1 2`

- رونوشت محتوای یک فایل در کلیپ بورد:

`copyq copy < {{path/to/file.txt}}`

- رونوشت یک عکس با فرمت JPEG در کلیپ بورد:

`copyq copy image/jpeg < {{path/to/image.jpg}}`
