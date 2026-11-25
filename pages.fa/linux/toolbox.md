# toolbox

> مدیریت محیط‌های خط فرمان کانتینری در لینوکس.
> برخی زیردستورها مانند `create` مستندات کاربرد جداگانه دارند.
> اطلاعات بیشتر: <https://manned.org/toolbox>.

- ورود به کانتینر Toolbx برای استفادهٔ تعاملی:

`toolbox enter {{container}}`

- حذف یک یا چند کانتینر:

`toolbox rm {{container1 container2 ...}}`

- حذف یک یا چند تصویر:

`toolbox rmi {{image1 image2 ...}}`

- نمایش راهنمای زیردستور مشخص (مانند `create`، `enter`، `rm` و غیره):

`toolbox help {{subcommand}}`

- نمایش راهنما:

`toolbox {{[-h|--help]}}`

- نمایش نسخه:

`toolbox --version`
