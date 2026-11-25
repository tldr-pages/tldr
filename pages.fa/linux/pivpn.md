# pivpn

> راه‌اندازی و مدیریت آسان OpenVPN با امنیت تقویت‌شده.
> در اصل برای Raspberry Pi طراحی شده است اما روی دستگاه‌های لینوکس دیگر نیز کار می‌کند.
> اطلاعات بیشتر: <https://docs.pivpn.io/openvpn/>.

- افزودن دستگاه کارخواه جدید:

`sudo pivpn add`

- فهرست کردن همهٔ دستگاه‌های کارخواه:

`sudo pivpn list`

- فهرست کردن دستگاه‌های متصل فعلی و آمار آن‌ها:

`sudo pivpn clients`

- لغو مجوز دستگاهی که قبلاً احراز هویت شده است:

`sudo pivpn revoke`

- حذف PiVPN:

`sudo pivpn uninstall`
