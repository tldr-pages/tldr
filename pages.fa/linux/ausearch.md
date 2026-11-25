# ausearch

> جست‌وجوی رویدادها در گزارش ممیزی لینوکس.
> بخشی از بستهٔ `audit` است.
> همچنین : `audit2why`, `audit2allow`, `aureport`.
> اطلاعات بیشتر: <https://manned.org/ausearch>.

- جست‌وجوی همهٔ رویدادهای رد دسترسی AVC در SELinux:

`sudo ausearch {{[-m|--message]}} avc`

- جست‌وجوی رویدادهای مربوط به یک فایل اجرایی مشخص:

`sudo ausearch {{[-c|--comm]}} {{httpd}}`

- جست‌وجوی رویدادهای مربوط به یک کاربر مشخص:

`sudo ausearch {{[-ui|--uid]}} {{1000}}`

- جست‌وجوی رویدادهای ۱۰ دقیقهٔ اخیر:

`sudo ausearch {{[-ts|--start]}} recent`

- جست‌وجوی تلاش‌های ناموفق برای ورود:

`sudo ausearch {{[-m|--message]}} user_login {{[-sv|--success]}} no`

- جست‌وجوی رویدادهای مربوط به یک فایل مشخص:

`sudo ausearch {{[-f|--file]}} {{path/to/file}}`

- نمایش نتایج در قالب خام برای پردازش بیشتر:

`sudo ausearch {{[-m|--message]}} avc --raw`
