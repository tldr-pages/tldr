# ltrace

> نمایش فراخوانی‌های کتابخانهٔ پویا توسط فرایند.
> اطلاعات بیشتر: <https://manned.org/ltrace>.

- چاپ (ردیابی) فراخوانی‌های کتابخانه‌ای فایل دودویی برنامه:

`ltrace {{path/to/program}}`

- شمارش فراخوانی‌های کتابخانه‌ای و چاپ خلاصه‌ای کاربردی در انتها:

`ltrace -c {{path/to/program}}`

- ردیابی فراخوانی‌های malloc و free، به‌جز موارد انجام‌شده توسط libc:

`ltrace -e malloc+free-@libc.so* {{path/to/program}}`

- نوشتن در فایل به‌جای ترمینال:

`ltrace {{[-o|--output]}} {{file}} {{path/to/program}}`
