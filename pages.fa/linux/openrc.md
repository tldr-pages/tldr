# openrc

> مدیر سرویس OpenRC.
> همچنین : `rc-status`, `rc-update`, `rc-service`.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/OpenRC>.

- تغییر به سطح اجرای مشخص:

`sudo openrc {{runlevel_name}}`

- تغییر به سطح اجرای مشخص بدون توقف سرویس‌های موجود:

`sudo openrc {{[-n|--no-stop]}} {{runlevel_name}}`
