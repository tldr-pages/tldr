# ahost

> ابزار جست‌وجوی DNS برای نمایش رکورد A یا AAAA مرتبط با یک نام میزبان یا آدرس IP.
> اطلاعات بیشتر: <https://manned.org/ahost>.

- چاپ رکورد `A` یا `AAAA` مرتبط با یک نام میزبان یا آدرس IP:

`ahost {{example.com}}`

- نمایش خروجی اضافی اشکال‌زدایی:

`ahost -d {{example.com}}`

- نمایش رکوردی با نوع مشخص:

`ahost -t {{a|aaaa|u}} {{example.com}}`
