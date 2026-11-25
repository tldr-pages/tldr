# powerstat

> اندازه‌گیری مصرف توان رایانه‌ای که باتری دارد یا از رابط RAPL پشتیبانی می‌کند.
> اطلاعات بیشتر: <https://manned.org/powerstat>.

- اندازه‌گیری توان با پیش‌فرض ۱۰ نمونه با فاصلهٔ ۱۰ ثانیه:

`powerstat`

- اندازه‌گیری توان با تعداد نمونه و فاصلهٔ دلخواه:

`powerstat {{interval}} {{number_of_samples}}`

- اندازه‌گیری توان با رابط RAPL شرکت Intel:

`powerstat -R {{interval}} {{number_of_samples}}`

- نمایش هیستوگرام اندازه‌گیری‌های توان:

`powerstat -H {{interval}} {{number_of_samples}}`

- فعال کردن همهٔ گزینه‌های جمع‌آوری آمار:

`powerstat -a {{interval}} {{number_of_samples}}`
