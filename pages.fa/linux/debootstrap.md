# debootstrap

> ایجاد یک سیستم پایهٔ دبیان.
> اطلاعات بیشتر: <https://wiki.debian.org/Debootstrap>.

- ایجاد سیستم نسخهٔ پایدار دبیان داخل دایرکتوری `debian-root`:

`sudo debootstrap stable {{path/to/debian-root}}/ http://deb.debian.org/debian`

- ایجاد یک سیستم حداقلی شامل فقط بسته‌های ضروری:

`sudo debootstrap --variant=minbase stable {{path/to/debian-root}}/`

- ایجاد یک سیستم Debian Unstable داخل دایرکتوری `sid-root` با یک مخزن آینهٔ محلی:

`sudo debootstrap sid {{path/to/sid-root}}/ {{file:///path/to/mirror}}/`

- تغییر به سیستم راه‌اندازی‌شده:

`sudo chroot {{path/to/root}}`

- فهرست کردن نسخه‌های موجود:

`ls /usr/share/debootstrap/scripts/`
