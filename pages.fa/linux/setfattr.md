# setfattr

> تنظیم ویژگی‌های گستردهٔ فایل.
> همچنین : `getfattr`.
> اطلاعات بیشتر: <https://manned.org/setfattr>.

- تنظیم نام ویژگی برای فایل:

`setfattr {{[-n|--name]}} user.{{attribute_name}} {{path/to/file}}`

- تنظیم مقدار تعریف‌شده توسط کاربر برای ویژگی گستردهٔ فایل:

`setfattr {{[-n|--name]}} user.{{attribute_name}} {{[-v|--value]}} "{{value}}" {{path/to/file}}`

- حذف ویژگی مشخص فایل:

`setfattr {{[-x|--remove]}} user.{{attribute_name}} {{path/to/file}}`
