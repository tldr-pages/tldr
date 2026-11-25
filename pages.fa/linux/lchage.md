# lchage

> نمایش یا تغییر سیاست رمز عبور کاربر.
> اطلاعات بیشتر: <https://manned.org/lchage>.

- غیرفعال کردن انقضای رمز عبور کاربر:

`sudo lchage --date -1 {{username}}`

- نمایش سیاست رمز عبور کاربر:

`sudo lchage --list {{username}}`

- الزام تغییر رمز عبور کاربر پس از تعداد روز مشخصی از آخرین تغییر رمز:

`sudo lchage --maxdays {{number_of_days}} {{username}}`

- آغاز هشدار به کاربر تعداد روز مشخصی پیش از انقضای رمز عبور:

`sudo lchage --warndays {{number_of_days}} {{username}}`
