# wine reg export

> صادرات کلیدها، مقادیر و داده‌ها از رجیستری Wine به فایل `.reg`.
> اطلاعات بیشتر: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-export>.

- صادرات کلید رجیستری و زیرکلیدهای آن به فایل:

`wine reg export '{{HKEY_CURRENT_USER\path\to\key}}' {{path/to/file.reg}}`

- صادرات کل یک hive رجیستری به فایل:

`wine reg export {{HKEY_CURRENT_USER}} {{path/to/file.reg}}`

- بازنویسی فایل خروجی در صورت وجود، بدون پرسش:

`wine reg export '{{HKEY_CURRENT_USER\path\to\key}}' {{path/to/file.reg}} /y`

- نمایش راهنما:

`wine reg export /?`
