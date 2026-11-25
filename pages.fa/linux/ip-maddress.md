# ip maddress

> مدیریت آدرس‌های multicast.
> اطلاعات بیشتر: <https://manned.org/ip-maddress>.

- فهرست کردن آدرس‌های multicast و تعداد برنامه‌های مشترک آن‌ها:

`ip {{[m|maddress]}}`

- فهرست کردن آدرس‌های مخصوص دستگاه:

`ip {{[m|maddress]}} {{[s|show]}} dev {{ethX}}`

- پیوستن ایستا به گروه multicast:

`sudo ip {{[m|maddress]}} {{[a|add]}} {{33:33:00:00:00:02}} dev {{ethX}}`

- ترک گروه multicast ایستا:

`sudo ip {{[m|maddress]}} {{[d|delete]}} {{33:33:00:00:00:02}} dev {{ethX}}`

- نمایش راهنما:

`ip {{[m|maddress]}} {{[h|help]}}`
