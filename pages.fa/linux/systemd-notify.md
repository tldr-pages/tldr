# systemd-notify

> اطلاع دادن تکمیل شروع و سایر تغییرات وضعیت سرویس به مدیر سرویس.
> این دستور خارج از اسکریپت‌های سرویس systemd کاربردی ندارد.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-notify.html>.

- اطلاع به systemd از تکمیل مقداردهی اولیه و شروع کامل سرویس؛ باید هنگام آمادگی سرویس برای پذیرش درخواست‌های ورودی فراخوانی شود:

`systemd-notify --booted`

- اعلام آمادگی سرویس به systemd برای رسیدگی به اتصال‌های ورودی یا انجام وظایف:

`systemd-notify --ready`

- ارائهٔ پیام وضعیت دلخواه به systemd (این اطلاعات با `systemctl status` نمایش داده می‌شود):

`systemd-notify --status "{{Add custom status message here...}}"`
