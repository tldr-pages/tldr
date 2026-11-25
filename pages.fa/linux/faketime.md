# faketime

> جعل زمان سیستم برای یک دستور.
> اطلاعات بیشتر: <https://manned.org/faketime>.

- جعل زمان به امشب پیش از چاپ نتیجهٔ `date`:

`faketime '{{today 23:30}}' {{date}}`

- باز کردن یک پوستهٔ جدید Bash که دیروز را تاریخ فعلی در نظر می‌گیرد:

`faketime '{{yesterday}}' {{bash}}`

- شبیه‌سازی عملکرد یک برنامه در شب جمعهٔ آینده:

`faketime '{{next Friday 1 am}}' {{path/to/program}}`

- اجرای برنامه در تاریخ و زمان مشخص:

`faketime '{{2020-01-01 12:00:00}}' {{program}}`
