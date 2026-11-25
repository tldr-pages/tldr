# dnsrecon

> ابزار شمارش و شناسایی DNS.
> اطلاعات بیشتر: <https://manned.org/dnsrecon>.

- پویش یک دامنه و ذخیرهٔ نتایج در پایگاه دادهٔ SQLite:

`dnsrecon {{[-d|--domain]}} {{example.com}} --db {{path/to/database.sqlite}}`

- پویش یک دامنه با تعیین سرور نام و انجام انتقال ناحیه:

`dnsrecon {{[-d|--domain]}} {{example.com}} {{[-n|--name_server]}} {{nameserver.example.com}} {{[-t|--type]}} axfr`

- پویش یک دامنه با حملهٔ جست‌وجوی فراگیر و واژه‌نامهٔ زیردامنه‌ها و نام میزبان‌ها:

`dnsrecon {{[-d|--domain]}} {{example.com}} {{[-D|--dictionary]}} {{path/to/dictionary.txt}} {{[-t|--type]}} brt`

- پویش یک دامنه با جست‌وجوی معکوس بازه‌های IP از رکورد SPF و ذخیرهٔ نتایج در فایل JSON:

`dnsrecon {{[-d|--domain]}} {{example.com}} -s {{[-j|--json]}}`

- پویش یک دامنه با شناسایی از طریق گوگل و ذخیرهٔ نتایج در فایل CSV:

`dnsrecon {{[-d|--domain]}} {{example.com}} -g {{[-c|--csv]}}`

- پویش یک دامنه با بررسی حافظهٔ نهان DNS:

`dnsrecon {{[-d|--domain]}} {{example.com}} {{[-t|--type]}} snoop {{[-n|--name_server]}} {{nameserver.example.com}} {{[-D|--dictionary]}} {{path/to/dictionary.txt}}`

- پویش یک دامنه با پیمایش ناحیه:

`dnsrecon {{[-d|--domain]}} {{example.com}} {{[-t|--type]}} zonewalk`
