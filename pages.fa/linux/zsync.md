# zsync

> بارگیری‌کنندهٔ جزئی یا تفاضلی فایل.
> از HTTPS پشتیبانی نمی‌شود؛ فقط از URLهای HTTP استفاده کنید.
> همچنین ببینید: `rsync`.
> اطلاعات بیشتر: <https://manned.org/zsync>.

- بارگیری فایل با فایل کنترل `.zsync`:

`zsync {{path/to/url.zsync}}`

- استفاده از فایل محلی به‌عنوان منبع برای جلوگیری از بارگیری دوبارهٔ بخش‌های تغییرنکرده:

`zsync -i {{path/to/existing_file}} {{path/to/url.zsync}}`

- ذخیرهٔ فایل به‌روزشده با نام مشخص:

`zsync -i {{path/to/existing_file}} -o {{path/to/new_file}} {{path/to/url.zsync}}`

- ادامهٔ بارگیری ناقص و نگه داشتن فایل موقت:

`zsync -k {{path/to/url.zsync}}`

- اجرا در حالت بی‌صدا با حداقل خروجی (بدون نوار پیشرفت، نرخ بارگیری یا زمان تخمینی باقی‌مانده):

`zsync -q {{path/to/url.zsync}}`
