# ip address

> زیردستور مدیریت آدرس IP.
> اطلاعات بیشتر: <https://manned.org/ip-address>.

- فهرست کردن واسط‌های شبکه و آدرس‌های IP مرتبط:

`ip {{[a|address]}}`

- فیلتر کردن برای نمایش فقط واسط‌های شبکهٔ فعال:

`ip {{[a|address]}} {{[s|show]}} up`

- نمایش اطلاعات واسط شبکهٔ مشخص:

`ip {{[a|address]}} {{[s|show]}} {{ethX}}`

- افزودن آدرس IP به واسط شبکه:

`sudo ip {{[a|address]}} {{[a|add]}} {{ip_address}} dev {{ethX}}`

- حذف آدرس IP از واسط شبکه:

`sudo ip {{[a|address]}} {{[d|delete]}} {{ip_address}} dev {{ethX}}`

- حذف همهٔ آدرس‌های IP در محدودهٔ مشخص از واسط شبکه:

`sudo ip {{[a|address]}} {{[f|flush]}} {{ethX}} scope {{global|host|link}}`
