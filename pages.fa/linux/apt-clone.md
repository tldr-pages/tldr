# apt-clone

> رونوشت‌گیری، پشتیبان‌گیری و بازیابی وضعیت بسته‌های یک سیستم مبتنی بر دبیان.
> اطلاعات بیشتر: <https://github.com/mvo5/apt-clone>.

- رونوشت‌گیری از وضعیت بسته‌های سیستم فعلی در یک دایرکتوری مشخص:

`apt-clone clone {{path/to/directory}}`

- ساخت فایل رونوشت (`.tar.gz`) برای پشتیبان‌گیری:

`apt-clone clone --destination {{path/to/backup.tar.gz}}`

- بازیابی وضعیت بسته‌ها از فایل رونوشت:

`apt-clone restore {{path/to/backup.tar.gz}}`

- نمایش اطلاعات یک فایل رونوشت (مانند نسخهٔ توزیع و معماری):

`apt-clone info {{path/to/backup.tar.gz}}`

- بررسی امکان بازیابی فایل رونوشت در سیستم فعلی:

`apt-clone restore {{path/to/backup.tar.gz}} --destination {{path/to/restore}}`
