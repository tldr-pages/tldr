# cryptcat

> انشعابی از Netcat با قابلیت رمزگذاری.
> اطلاعات بیشتر: <https://manned.org/cryptcat>.

- گوش دادن روی درگاه مشخص‌شده با `-l` و `-p` و چاپ داده‌های دریافتی:

`cryptcat -k {{password}} -l -p {{port}}`

- اتصال به یک درگاه مشخص:

`cryptcat -k {{password}} {{ip_address}} {{port}}`

- تعیین مهلت زمانی با `-w`:

`cryptcat -k {{password}} -w {{timeout_in_seconds}} {{ip_address}} {{port}}`

- پویش درگاه‌های باز یک میزبان مشخص با `-z`:

`cryptcat -v -z {{ip_address}} {{port}}`

- عمل کردن به‌عنوان پراکسی و انتقال داده از درگاه TCP محلی به میزبان راه دور مشخص:

`cryptcat -k {{password}} -l -p {{local_port}} | cryptcat -k {{password}} {{hostname}} {{remote_port}}`
