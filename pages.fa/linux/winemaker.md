# winemaker

> تولید فایل‌های ساخت برای انتقال کد منبع Windows به برنامهٔ Winelib.
> اطلاعات بیشتر: <https://manned.org/winemaker>.

- تولید فایل‌های ساخت برای درخت کد منبع (با فرض برنامهٔ گرافیکی):

`winemaker {{path/to/source_directory}}`

- در نظر گرفتن هدف به‌عنوان برنامهٔ کنسولی:

`winemaker --console {{path/to/source_directory}}`

- در نظر گرفتن هدف به‌عنوان DLL:

`winemaker --dll {{path/to/source_directory}}`

- تولید فایل‌های ساخت بدون تغییر یا تغییر نام فایل‌های منبع اصلی:

`winemaker --nosource-fix {{path/to/source_directory}}`

- پردازش پروژه‌ای که از MFC استفاده می‌کند:

`winemaker --mfc {{path/to/source_directory}}`

- نمایش راهنما:

`winemaker --help`
