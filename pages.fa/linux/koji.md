# koji

> تعامل با kojihub.
> برخی زیردستورها مانند `build`، `tag-build`، `download-build`، `buildinfo` و `call` مستندات کاربرد جداگانه دارند.
> اطلاعات بیشتر: <https://docs.pagure.org/koji/>.

- اجرای زیردستور koji:

`koji {{subcommand}}`

- معرفی خود برای آزمودن اتصال به kojihub:

`koji moshimoshi`

- نمایش راهنمای گزینه‌های سراسری:

`koji {{[-h|--help]}}`

- نمایش راهنما برای دریافت همهٔ دستورهای موجود:

`koji help`

- نمایش راهنمای زیردستور مشخص (مانند `build`، `tag-build`، `download-build`، `buildinfo` یا `call`):

`koji {{subcommand}} {{[-h|--help]}}`

- نمایش نسخه:

`koji version`
