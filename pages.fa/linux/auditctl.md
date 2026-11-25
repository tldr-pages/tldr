# auditctl

> ابزاری برای کنترل رفتار، دریافت وضعیت و مدیریت قواعد سامانهٔ ممیزی لینوکس.
> اطلاعات بیشتر: <https://manned.org/auditctl>.

- نمایش وضعیت سامانهٔ ممیزی با `-s`:

`sudo auditctl -s`

- فهرست کردن همهٔ قواعد ممیزی بارگذاری‌شدهٔ فعلی با `-l`:

`sudo auditctl -l`

- حذف همهٔ قواعد ممیزی با `-D`:

`sudo auditctl -D`

- فعال یا غیرفعال کردن سامانهٔ ممیزی با `-e`:

`sudo auditctl -e {{1|0}}`

- پایش تغییرات یک فایل:

`sudo auditctl -a always,exit -F arch=b64 -F path=/{{path/to/file}} -F perm=wa`

- پایش بازگشتی تغییرات یک دایرکتوری:

`sudo auditctl -a always,exit -F arch=b64 -F dir=/{{path/to/directory}}/ -F perm=wa`

- نمایش راهنما با `-h`:

`auditctl -h`
