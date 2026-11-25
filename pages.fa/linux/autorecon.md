# autorecon

> ابزار چندریسه‌ای شناسایی شبکه که شمارش خودکار سرویس‌ها را انجام می‌دهد.
> اطلاعات بیشتر: <https://github.com/AutoRecon/AutoRecon>.

- شناسایی میزبان‌های هدف (نتایج مفصل پویش در `results` ذخیره می‌شوند):

`sudo autorecon {{host_or_ip1,host_or_ip2,...}}`

- شناسایی هدف‌های موجود در یک فایل:

`sudo autorecon {{[-t|--target-file]}} {{path/to/file}}`

- نوشتن نتایج در یک دایرکتوری دیگر:

`sudo autorecon {{[-o|--output]}} {{path/to/results}} {{host_or_ip1,host_or_ip2,...}}`

- محدود کردن پویش به درگاه‌ها و پروتکل‌های مشخص (`T` برای TCP، `U` برای UDP و `B` برای هر دو):

`sudo autorecon {{[-p|--ports]}} {{T:21-25,80,443,U:53,B:123}} {{host_or_ip1,host_or_ip2,...}}`
