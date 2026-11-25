# dnsmap

> پویش یک دامنه برای زیردامنه‌های متداول، مانند smtp.domain.org.
> اطلاعات بیشتر: <https://github.com/resurrecting-open-source-projects/dnsmap>.

- پویش زیردامنه‌ها با فهرست واژه‌های داخلی:

`dnsmap {{example.com}}`

- تعیین فهرستی از زیردامنه‌ها برای بررسی:

`dnsmap {{example.com}} -w {{path/to/wordlist.txt}}`

- ذخیرهٔ نتایج در فایل CSV:

`dnsmap {{example.com}} -c {{path/to/file.csv}}`

- نادیده گرفتن ۲ آدرس IP با نتیجهٔ مثبت کاذب (حداکثر ۵ مورد ممکن است):

`dnsmap {{example.com}} -i {{123.45.67.89,98.76.54.32}}`
