# stegsnow

> ابزار پنهان‌نگاری برای مخفی کردن و استخراج پیام‌ها در فایل‌های متنی با کدگذاری tab و فاصله.
> اطلاعات بیشتر: <https://darkside.com.au/snow/manual.html>.

- استخراج پیام از فایل:

`stegsnow {{path/to/file.txt}}`

- استخراج پیام فشرده و محافظت‌شده با رمز عبور از فایل:

`stegsnow -C -p {{password}} {{path/to/file.txt}}`

- تعیین ظرفیت تقریبی ذخیره‌سازی فایل با طول خط کمتر از ۷۲:

`stegsnow -S -l 72 {{path/to/file.txt}}`

- پنهان کردن پیام در متن فایل و ذخیرهٔ نتیجه:

`stegsnow -m '{{message}}' {{path/to/file.txt}} {{path/to/result.txt}}`

- پنهان کردن محتوای فشردهٔ فایل پیام در متن فایل و ذخیرهٔ نتیجه:

`stegsnow -C -f '{{path/to/message.txt}}' {{path/to/file.txt}} {{path/to/result.txt}}`

- پنهان کردن پیام فشرده و محافظت‌شده با رمز عبور در متن فایل و ذخیرهٔ نتیجه:

`stegsnow -C -p {{password}} -m '{{message}}' {{path/to/file.txt}} {{path/to/result.txt}}`
