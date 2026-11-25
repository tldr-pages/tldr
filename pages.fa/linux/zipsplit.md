# zipsplit

> تقسیم بایگانی Zip به بایگانی‌های Zip کوچک‌تر.
> اطلاعات بیشتر: <https://manned.org/zipsplit>.

- تقسیم بایگانی Zip به بخش‌هایی با حداکثر ۳۶۰۰۰ بایت (۳۶ MB):

`zipsplit {{path/to/archive.zip}}`

- استفاده از تعداد بایت مشخص به‌عنوان حد هر بخش:

`zipsplit -n {{size}} {{path/to/archive.zip}}`

- مکث بین ایجاد هر بخش:

`zipsplit -p -n {{size}} {{path/to/archive.zip}}`

- خروجی بایگانی‌های Zip کوچک‌تر در دایرکتوری مشخص:

`zipsplit -b {{path/to/output_directory}} -n {{size}} {{path/to/archive.zip}}`
