# jpegtran

> انجام تبدیل بدون افت روی فایل‌های JPEG.
> اطلاعات بیشتر: <https://manned.org/jpegtran>.

- آینه کردن تصویر به‌صورت افقی یا عمودی:

`jpegtran {{[-f|-flip]}} {{horizontal|vertical}} {{path/to/image.jpg}} >{{path/to/output.jpg}}`

- چرخاندن تصویر به‌اندازهٔ ۹۰، ۱۸۰ یا ۲۷۰ درجه در جهت ساعت‌گرد:

`jpegtran {{[-ro|-rotate]}} {{90|180|270}} {{path/to/image.jpg}} >{{path/to/output.jpg}}`

- ترانهاده کردن تصویر نسبت به محور بالا-چپ به پایین-راست:

`jpegtran -transpose {{path/to/image.jpg}} >{{path/to/output.jpg}}`

- ترانهادهٔ معکوس تصویر نسبت به محور بالا-راست به پایین-چپ:

`jpegtran -transverse {{path/to/image.jpg}} >{{path/to/output.jpg}}`

- تبدیل تصویر به خاکستری:

`jpegtran {{[-g|-grayscale]}} {{path/to/image.jpg}} >{{path/to/output.jpg}}`

- برش تصویر به ناحیهٔ مستطیلی با عرض `W` و ارتفاع `H` از گوشهٔ بالا-چپ و ذخیرهٔ خروجی در فایل مشخص:

`jpegtran -crop {{W}}x{{H}} -outfile {{path/to/output.jpg}} {{path/to/image.jpg}}`

- برش تصویر به ناحیهٔ مستطیلی با عرض `W` و ارتفاع `H` از نقطهٔ `X` و `Y` نسبت به گوشهٔ بالا-چپ:

`jpegtran -crop {{W}}x{{H}}+{{X}}+{{Y}} {{path/to/image.jpg}} >{{path/to/output.jpg}}`
