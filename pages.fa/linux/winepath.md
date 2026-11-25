# winepath

> تبدیل مسیر فایل‌ها بین قالب‌های Windows و Unix برای پیشوند Wine.
> اطلاعات بیشتر: <https://manned.org/winepath>.

- تبدیل مسیر Windows به مسیر Unix:

`winepath {{[-u|--unix]}} '{{C:\path\to\file}}'`

- تبدیل مسیر Unix به مسیر بلند Windows:

`winepath {{[-w|--windows]}} {{path/to/file}}`

- تبدیل مسیر کوتاه Windows به قالب بلند برای فایل موجود:

`winepath {{[-l|--long]}} '{{C:\PROGRA~1}}'`

- تبدیل مسیر بلند Windows به قالب کوتاه برای فایل موجود:

`winepath {{[-s|--short]}} '{{C:\Program Files}}'`

- جدا کردن مسیرهای خروجی با نویسهٔ null به‌جای خط جدید:

`winepath {{[-u|--unix]}} -0 {{path1 path2 ...}}`

- نمایش راهنما:

`winepath {{[-h|--help]}}`
