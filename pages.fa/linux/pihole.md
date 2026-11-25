# pihole

> مدیریت سرور DNS مسدودکنندهٔ تبلیغات Pi-hole.
> اطلاعات بیشتر: <https://docs.pi-hole.net/main/pihole-command/>.

- بررسی وضعیت Pi-hole:

`pihole status`

- به‌روزرسانی Pi-hole و Gravity:

`sudo pihole {{[-up|updatePihole]}}`

- شروع یا توقف سرویس:

`pihole {{enable|disable}}`

- به‌روزرسانی فهرست‌ها و تخلیهٔ حافظهٔ نهان بدون راه‌اندازی مجدد سرور DNS:

`pihole reloaddns`

- به‌روزرسانی فهرست دامنه‌های ارائه‌دهندهٔ تبلیغات:

`pihole {{[-g|updateGravity]}}`

- اجازه یا منع دامنهٔ مشخص:

`pihole {{allow|deny}} {{example.com}}`

- جست‌وجوی دامنه در فهرست‌ها:

`pihole {{[-q|query]}} {{example.com}}`

- باز کردن گزارش بلادرنگ اتصال‌ها:

`pihole {{[-t|tail]}}`
