# duperemove

> یافتن extentهای تکراری سیستم فایل و در صورت تمایل زمان‌بندی حذف تکرار آن‌ها.
> extent بخش کوچکی از یک فایل در سیستم فایل است.
> در برخی سیستم‌های فایل، هنگامی که بخش‌هایی از محتوای فایل‌ها یکسان باشند، می‌توان چند بار به یک extent ارجاع داد.
> اطلاعات بیشتر: <https://markfasheh.github.io/duperemove/>.

- جست‌وجو و نمایش extentهای تکراری در یک دایرکتوری:

`duperemove -r {{path/to/directory}}`

- حذف تکرار extentهای تکراری در سیستم فایل Btrfs یا XFS (آزمایشی):

`duperemove -r -d {{path/to/directory}}`

- استفاده از فایل هش برای ذخیرهٔ هش extentها (مصرف حافظه کمتر است و در اجراهای بعدی قابل استفادهٔ مجدد است):

`duperemove -r -d --hashfile={{path/to/hashfile}} {{path/to/directory}}`

- محدود کردن ریسه‌های ورودی/خروجی برای مرحلهٔ هش و حذف تکرار و ریسه‌های پردازنده برای مرحلهٔ یافتن extentهای تکراری:

`duperemove -r -d --hashfile={{path/to/hashfile}} --io-threads={{n}} --cpu-threads={{n}} {{path/to/directory}}`
