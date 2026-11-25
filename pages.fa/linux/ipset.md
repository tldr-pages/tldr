# ipset

> ایجاد مجموعه‌های IP برای قوانین دیوار آتش.
> اطلاعات بیشتر: <https://manned.org/ipset>.

- ایجاد مجموعهٔ IP خالی برای نگهداری آدرس‌های IP:

`ipset create {{set_name}} hash:ip`

- از بین بردن مجموعهٔ IP مشخص:

`ipset destroy {{set_name}}`

- افزودن آدرس IP به مجموعهٔ مشخص:

`ipset add {{set_name}} {{192.168.1.25}}`

- حذف آدرس IP مشخص از مجموعه:

`ipset del {{set_name}} {{192.168.1.25}}`

- ذخیرهٔ مجموعهٔ IP:

`ipset save {{set_name}} >{{path/to/ip_set}}`
