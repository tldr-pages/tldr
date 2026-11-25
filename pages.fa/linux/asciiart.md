# asciiart

> تبدیل تصاویر به ASCII.
> اطلاعات بیشتر: <https://github.com/nodanaonlyzuul/asciiart#in-the-command-line>.

- خواندن یک تصویر از فایل و چاپ آن به‌صورت ASCII:

`asciiart {{path/to/image.jpg}}`

- خواندن یک تصویر از URL و چاپ آن به‌صورت ASCII:

`asciiart {{www.example.com/image.jpg}}`

- انتخاب عرض خروجی (پیش‌فرض ۱۰۰ است):

`asciiart {{[-w|--width]}} {{50}} {{path/to/image.jpg}}`

- رنگی کردن خروجی ASCII:

`asciiart {{[-c|--color]}} {{path/to/image.jpg}}`

- انتخاب قالب خروجی (قالب پیش‌فرض متن است):

`asciiart {{[-f|--format]}} {{text|html}} {{path/to/image.jpg}}`

- معکوس کردن نگاشت نویسه‌ها:

`asciiart {{[-i|--invert-chars]}} {{path/to/image.jpg}}`
