# ip tuntap

> مدیریت واسط‌های شبکهٔ مجازی TUN/TAP.
> اطلاعات بیشتر: <https://baturin.org/docs/iproute2/#ip-tuntap>.

- نمایش همهٔ دستگاه‌های TUN/TAP موجود:

`ip {{[tunt|tuntap]}}`

- ایجاد دستگاه TUN با نام مشخص:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tun0}} {{[m|mode]}} {{[t|tun]}}`

- ایجاد دستگاه TAP با نام مشخص:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tap0}} {{[m|mode]}} {{[ta|tap]}}`

- حذف دستگاه TUN یا TAP:

`sudo ip {{[tunt|tuntap]}} {{[d|delete]}} {{[d|dev]}} {{tun0|tap0}} {{[m|mode]}} {{tun|tap}}`

- تنظیم مالک (UID) دستگاه TUN/TAP:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tun0|tap0}} {{[m|mode]}} {{tun|tap}} {{[u|user]}} {{username}}`

- تنظیم مالک (UID) و گروه (GID) دستگاه TUN/TAP:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tun0|tap0}} {{[m|mode]}} {{tun|tap}} {{[u|user]}} {{username}} {{[g|group]}} {{group_name}}`
