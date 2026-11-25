# systemd-creds

> فهرست، نمایش، رمزگذاری و رمزگشایی اطلاعات ورود سرویس.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-creds.html>.

- رمزگذاری فایل و تنظیم نام مشخص:

`systemd-creds encrypt --name {{name}} {{path/to/input_file}} {{path/to/output}}`

- رمزگشایی دوبارهٔ فایل:

`systemd-creds decrypt {{path/to/input_file}} {{path/to/output_file}}`

- رمزگذاری متن از `stdin`:

`echo -n {{text}} | systemd-creds encrypt --name {{name}} - {{path/to/output}}`

- رمزگذاری متن و افزودن آن به فایل `.service` (اطلاعات ورود در `$CREDENTIALS_DIRECTORY` موجود خواهند بود):

`echo -n {{text}} | systemd-creds encrypt --name {{name}} --pretty - - >>{{service}}`

- ایجاد اطلاعات ورود معتبر فقط تا برچسب زمانی مشخص:

`systemd-creds encrypt --not-after "{{timestamp}}" {{path/to/input_file}} {{path/to/output_file}}`
