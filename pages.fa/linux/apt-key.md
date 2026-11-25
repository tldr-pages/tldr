# apt-key

> ابزار مدیریت کلید برای مدیر بستهٔ APT در دبیان و اوبونتو.
> توجه: این دستور منسوخ شده است (به جز استفاده از `apt-key del` در اسکریپت‌های نگهدارنده).
> اطلاعات بیشتر: <https://manned.org/apt-key>.

- فهرست کردن کلیدهای مورد اعتماد:

`apt-key list`

- افزودن یک کلید به مخزن کلیدهای مورد اعتماد:

`apt-key add {{public_key_file.asc}}`

- حذف یک کلید از مخزن کلیدهای مورد اعتماد:

`apt-key del {{key_id}}`

- افزودن یک کلید راه دور به مخزن کلیدهای مورد اعتماد:

`wget {{[-qO|--quiet --output-document]}} - {{https://host.tld/filename.key}} | apt-key add -`

- افزودن یک کلید از سرور کلید فقط با شناسهٔ کلید:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{key_id}}`
