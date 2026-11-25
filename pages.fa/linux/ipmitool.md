# ipmitool

> ارتباط با رابط مدیریت هوشمند پلتفرم (IPMI).
> اطلاعات بیشتر: <https://manned.org/ipmitool>.

- شروع درایور IPMI برای اتصال‌های محلی:

`systemctl start ipmidrv`

- باز کردن پوستهٔ IPMI روی سخت‌افزار محلی:

`sudo ipmitool shell`

- باز کردن پوستهٔ IPMI روی میزبان راه دور:

`ipmitool -H {{ip_address}} -U {{user_name}} shell`
