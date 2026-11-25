# alien

> تبدیل بسته‌های نصب مختلف به قالب‌های دیگر.
> همچنین : `debtap`.
> اطلاعات بیشتر: <https://manned.org/alien>.

- تبدیل یک فایل نصب مشخص به قالب دبیان (پسوند `.deb`):

`sudo alien {{[-d|--to-deb]}} {{path/to/file}}`

- تبدیل یک فایل نصب مشخص به قالب رد هت (پسوند `.rpm`):

`sudo alien {{[-r|--to-rpm]}} {{path/to/file}}`

- تبدیل یک فایل نصب مشخص به فایل نصب Slackware (پسوند `.tgz`):

`sudo alien {{[-t|--to-tgz]}} {{path/to/file}}`

- تبدیل یک فایل نصب مشخص به قالب دبیان و نصب آن روی سیستم:

`sudo alien {{[-d|--to-deb]}} {{[-i|--install]}} {{path/to/file}}`
