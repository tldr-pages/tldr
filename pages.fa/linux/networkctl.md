# networkctl

> پرس‌وجوی وضعیت پیوندهای شبکه.
> مدیریت پیکربندی شبکه با `systemd-networkd`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/networkctl.html>.

- فهرست کردن پیوندهای موجود همراه با وضعیت آن‌ها:

`networkctl`

- نمایش وضعیت کلی شبکه:

`networkctl status`

- فعال کردن دستگاه‌های شبکه:

`sudo networkctl up {{interface1 interface2 ...}}`

- غیرفعال کردن دستگاه‌های شبکه:

`sudo networkctl down {{interface1 interface2 ...}}`

- تمدید پیکربندی‌های پویا (مانند آدرس‌های IP دریافت‌شده از سرور DHCP):

`sudo networkctl renew {{interface1 interface2 ...}}`

- بارگذاری مجدد فایل‌های پیکربندی (`.netdev` و `.network`):

`sudo networkctl reload`

- پیکربندی مجدد واسط‌های شبکه (اگر پیکربندی را ویرایش کرده‌اید ابتدا باید `networkctl reload` را فراخوانی کنید):

`sudo networkctl reconfigure {{interface1 interface2 ...}}`
