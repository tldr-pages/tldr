# nmtui

> رابط کاربری متنی برای کنترل NetworkManager.
> برای پیمایش از `<ArrowKeys>` و برای انتخاب گزینه از `<Enter>` استفاده کنید.
> همچنین ببینید: `nmcli`.
> اطلاعات بیشتر: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmtui.html>.

- باز کردن رابط کاربری:

`nmtui`

- فهرست کردن اتصال‌های موجود با امکان فعال یا غیرفعال کردن آن‌ها:

`nmtui connect`

- اتصال به شبکهٔ مشخص:

`nmtui connect {{name|uuid|device|ssid}}`

- ویرایش، افزودن یا حذف شبکهٔ مشخص:

`nmtui edit {{name|id}}`

- تنظیم نام میزبان سیستم:

`nmtui hostname`
