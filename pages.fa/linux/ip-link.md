# ip link

> مدیریت واسط‌های شبکه.
> اطلاعات بیشتر: <https://manned.org/ip-link>.

- نمایش اطلاعات همهٔ واسط‌های شبکه:

`ip {{[l|link]}}`

- نمایش اطلاعات واسط شبکهٔ مشخص:

`ip {{[l|link]}} {{[sh|show]}} {{ethX}}`

- فعال یا غیرفعال کردن واسط شبکه:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} {{up|down}}`

- دادن نامی معنادار به واسط شبکه:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} {{[al|alias]}} "{{LAN Interface}}"`

- تغییر آدرس MAC واسط شبکه:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} {{[a|address]}} {{ff:ff:ff:ff:ff:ff}}`

- تغییر اندازهٔ MTU واسط شبکه برای استفاده از قاب‌های جامبو:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} mtu {{9000}}`

- تنظیم وضعیت حالت promiscuous دستگاه:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} promisc {{on|off}}`

- حذف دستگاه:

`sudo ip {{[l|link]}} {{[d|delete]}} {{ethX}}`
