# trap

> اجرای دستور هنگام رویداد.
> اطلاعات بیشتر: <https://www.gnu.org/software/bash/manual/bash.html#index-trap>.

- فهرست کردن نام رویدادهای موجود (مانند `SIGWINCH`):

`trap -l`

- فهرست کردن دستورها و نام رویدادهای مورد انتظار:

`trap`

- اجرای دستور هنگام دریافت سیگنال:

`trap 'echo "Caught signal {{SIGHUP}}"' {{[1|SIGHUP]}}`

- حذف دستورها:

`trap - {{SIGHUP SIGINT ...}}`

- نادیده گرفتن سیگنال:

`trap '' {{[2|SIGINT]}}`

- اجرای دستور هنگام خروج پوستهٔ فعلی:

`trap '{{echo "Initiating cleanup"}}' EXIT`

- اجرای دستور پیش از هر دستور:

`trap '{{echo "Debug output"}}' DEBUG`

- نمایش راهنما:

`help trap`
