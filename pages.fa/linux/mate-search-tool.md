# mate-search-tool

> جست‌وجوی فایل‌ها در محیط دسکتاپ MATE.
> اطلاعات بیشتر: <https://manned.org/mate-search-tool>.

- جست‌وجوی فایل‌هایی که نامشان حاوی رشتهٔ مشخص است در دایرکتوری مشخص:

`mate-search-tool --named={{string}} --path={{path/to/directory}}`

- جست‌وجوی فایل‌ها بدون انتظار برای تأیید کاربر:

`mate-search-tool --start --named={{string}} --path={{path/to/directory}}`

- جست‌وجوی فایل‌هایی که نامشان با `regex` مشخص مطابقت دارد:

`mate-search-tool --start --regex={{string}} --path={{path/to/directory}}`

- تنظیم ترتیب مرتب‌سازی نتایج جست‌وجو:

`mate-search-tool --start --named={{string}} --path={{path/to/directory}} --sortby={{name|folder|size|type|date}}`

- تنظیم ترتیب مرتب‌سازی نزولی:

`mate-search-tool --start --named={{string}} --path={{path/to/directory}} --descending`

- جست‌وجوی فایل‌های متعلق به کاربر یا گروه مشخص:

`mate-search-tool --start --{{user|group}}={{value}} --path={{path/to/directory}}`
