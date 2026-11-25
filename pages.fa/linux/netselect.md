# netselect

> آزمون سرعت برای انتخاب سرور شبکهٔ سریع.
> اطلاعات بیشتر: <https://manned.org/netselect>.

- انتخاب سرور با کمترین تأخیر:

`sudo netselect {{host_1 host_2 ...}}`

- نمایش حل نام سرور و آمار:

`sudo netselect -vv {{host_1 host_2 ...}}`

- تعیین حداکثر TTL (زمان حیات):

`sudo netselect -m {{10}} {{host_1 host_2 ...}}`

- چاپ `n` سرور سریع‌تر از میان میزبان‌ها:

`sudo netselect -s {{n}} {{host_1 host_2 host_3 ...}}`

- نمایش راهنما:

`netselect`
