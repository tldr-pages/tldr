# apk

> ابزار مدیریت بستهٔ آلپاین لینوکس.
> اطلاعات بیشتر: <https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper>.

- به‌روزرسانی فهرست‌های مخازن و ارتقای همهٔ بسته‌ها:

`apk upgrade {{[-U|--update-cache]}}`

- فقط به‌روزرسانی فهرست‌های مخازن:

`apk update`

- نصب یک بستهٔ جدید:

`apk add {{package}}`

- حذف یک بسته:

`apk del {{package}}`

- تعمیر یا نصب مجدد یک بسته بدون تغییر وابستگی‌های اصلی:

`apk fix {{package}}`

- جست‌وجوی بسته‌ها با یک کلیدواژه در نام و فهرست کردن نتایج همراه با توضیحات:

`apk search {{[-v|--verbose]}} {{keyword}}`

- جست‌وجوی بسته‌ها با یک کلیدواژه در توضیحات:

`apk search {{[-d|--description]}} {{keyword}}`

- نمایش اطلاعات یک بستهٔ مشخص:

`apk info {{package}}`
