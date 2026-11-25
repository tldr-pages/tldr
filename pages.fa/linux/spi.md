# spi

> مدیر فرابسته که هم بسته‌ها و هم slackbuildها را مدیریت می‌کند.
> اطلاعات بیشتر: <https://github.com/gapan/spi/blob/master/man/spi.t2t>.

- به‌روزرسانی فهرست بسته‌ها و slackbuildهای موجود:

`spi {{[-u|--update]}}`

- نصب بسته یا slackbuild:

`spi {{[-i|--install]}} {{package/slackbuild_name}}`

- ارتقای همهٔ بسته‌های نصب‌شده به جدیدترین نسخه‌های موجود:

`spi {{[-U|--upgrade]}}`

- یافتن بسته‌ها یا slackbuildها با نام بسته یا توضیح:

`spi {{search_terms}}`

- نمایش اطلاعات بسته یا slackbuild:

`spi --show {{package/slackbuild_name}}`

- پاک‌سازی حافظهٔ نهان محلی بسته‌ها و slackbuildها:

`spi --clean`
