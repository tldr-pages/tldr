# strace

> ابزار عیب‌یابی برای ردیابی فراخوانی‌های سیستم.
> همچنین ببینید: `fatrace`.
> اطلاعات بیشتر: <https://manned.org/strace>.

- شروع ردیابی فرایند مشخص با PID آن:

`sudo strace {{[-p|--attach]}} {{process_id}}`

- ردیابی فرایند و فیلتر خروجی بر اساس عبارت فراخوانی سیستم:

`sudo strace {{[-p|--attach]}} {{process_id}} -e {{system_call,system_call2,...}}`

- شمارش زمان، فراخوانی‌ها و خطاها برای هر فراخوانی سیستم و گزارش خلاصه هنگام خروج برنامه:

`sudo strace {{[-p|--attach]}} {{process_id}} {{[-c|--summary-only]}}`

- نمایش زمان صرف‌شده در هر فراخوانی سیستم و تعیین حداکثر اندازهٔ رشته برای چاپ:

`sudo strace {{[-p|--attach]}} {{process_id}} {{[-T|--syscall-times]}} {{[-s|--string-limit]}} {{32}}`

- شروع ردیابی برنامه با اجرای آن:

`strace {{program}}`

- شروع ردیابی عملیات فایل برنامه:

`strace -e trace=file {{program}}`

- شروع ردیابی عملیات شبکهٔ برنامه و همهٔ فرایندهای منشعب و فرزند آن و ذخیرهٔ خروجی در فایل:

`strace {{[-f|--follow-forks]}} -e trace=network {{[-o|--output]}} {{trace.txt}} {{program}}`
