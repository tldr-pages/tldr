# gpm

> فعال کردن پشتیبانی ماوس برای کنسول مجازی لینوکس.
> اطلاعات بیشتر: <https://manned.org/gpm>.

- شروع gpm با ماوس PS/2 مشخص‌شده با `-m` و نوع ps2 با `-t`:

`sudo gpm -m /dev/input/mice -t ps2`

- شروع gpm با ماوس سریال مایکروسافت مشخص‌شده با `-m` و نوع ms با `-t`:

`sudo gpm -m /dev/ttyS0 -t ms`

- شروع gpm با ماوس و نوع مشخص با `-m` و `-t` در پیش‌زمینه برای اشکال‌زدایی با `-D`:

`sudo gpm -m {{path/to/mouse_device}} -t {{mouse_type}} -D`

- خاتمه دادن به gpm در حال اجرا با `-k`:

`sudo gpm -k`

- شروع gpm با ماوس و نوع مشخص با `-m` و `-t` در حالت تکرارکننده با `-R` برای سازگاری با سرور X:

`sudo gpm -m {{path/to/mouse_device}} -t {{mouse_type}} -R`

- فهرست کردن انواع موجود ماوس با `-t`:

`gpm -t help`
