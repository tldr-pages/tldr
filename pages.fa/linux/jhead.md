# jhead

> تغییر برچسب زمانی تصویر و داده‌های EXIF.
> اطلاعات بیشتر: <https://www.sentex.net/~mwandel/jhead/usage.html>.

- نمایش همهٔ داده‌های EXIF:

`jhead {{path/to/image.jpg}}`

- تنظیم تاریخ و زمان فایل به تاریخ ایجاد EXIF (تاریخ ایجاد فایل تغییر می‌کند):

`jhead -ft {{path/to/image.jpg}}`

- تنظیم زمان EXIF به تاریخ و زمان فایل (داده‌های EXIF تغییر می‌کنند):

`jhead -dsft {{path/to/image.jpg}}`

- تغییر نام همهٔ فایل‌های JPEG بر اساس تاریخ ایجاد EXIF به `YYYY_MM_DD-HH_MM_SS.jpg`:

`jhead -n%Y_%m_%d-%H_%M_%S *.jpg`

- چرخاندن بدون افت همهٔ تصاویر JPEG به‌اندازهٔ ۹۰، ۱۸۰ یا ۲۷۰ درجه بر اساس برچسب جهت EXIF:

`jhead -autorot *.jpg`

- به‌روزرسانی همهٔ برچسب‌های زمانی EXIF (قالب: +- ساعت:دقیقه:ثانیه) (مثلاً در صورت فراموشی تغییر منطقهٔ زمانی دوربین، حذف ۱ ساعت از برچسب‌ها):

`jhead -ta-1:00:00 *.jpg`

- حذف همهٔ داده‌های EXIF (از جمله تصاویر بندانگشتی):

`jhead -purejpg {{path/to/image.jpg}}`
