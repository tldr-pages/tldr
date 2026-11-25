# ufw limit

> محدود کردن نرخ اتصال برای منع IP دارای ۶ تلاش یا بیشتر در ۳۰ ثانیه.
> اطلاعات بیشتر: <https://manned.org/ufw>.

- شبیه‌سازی قانون بدون اعمال آن:

`sudo ufw --dry-run limit {{profile}}`

- محدود کردن نرخ سرویس مشخص با پروفایل:

`sudo ufw limit {{profile}}`

- محدود کردن نرخ پورت و پروتکل مشخص:

`sudo ufw limit {{22}}/{{tcp}}`

- محدود کردن نرخ فقط از آدرس مبدأ یا زیرشبکهٔ مشخص:

`sudo ufw limit from {{192.168.0.0/16}} to any port {{22}} proto {{tcp}}`

- محدود کردن نرخ روی واسط شبکهٔ مشخص:

`sudo ufw limit in on {{eth0}} to any port {{22}}`

- حذف قانون محدودیت:

`sudo ufw delete limit {{service|port}}/{{tcp}}`
