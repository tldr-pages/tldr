# lrztar

> واسطی برای `lrzip` جهت ساده‌سازی فشرده‌سازی دایرکتوری‌ها.
> همچنین : `tar`, `lrzuntar`, `lrunzip`.
> اطلاعات بیشتر: <https://manned.org/lrztar>.

- بایگانی دایرکتوری با `tar` و سپس فشرده‌سازی آن:

`lrztar {{path/to/directory}}`

- بایگانی دایرکتوری با `tar` و سپس فشرده‌سازی با ZPAQ (فشرده‌سازی بسیار زیاد اما بسیار کند):

`lrztar {{[-z|--zpaq]}} {{path/to/directory}}`

- تعیین فایل خروجی:

`lrztar {{[-o|--outfile]}} {{path/to/file}} {{path/to/directory}}`

- تعیین تعداد رشته‌های پردازنده برای استفاده:

`lrztar {{[-p|--threads]}} {{8}} {{path/to/directory}}`

- اجبار به بازنویسی فایل‌های موجود:

`lrztar {{[-f|--force]}} {{path/to/directory}}`
