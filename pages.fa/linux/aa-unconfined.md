# aa-unconfined

> فهرست کردن فرایندهایی با درگاه‌های TCP/UDP باز که پروفایل AppArmor برای آن‌ها بارگذاری نشده است.
> اطلاعات بیشتر: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-unconfined.8>.

- فهرست کردن فرایندهای بدون محدودیت با دستور `ss` (پیش‌فرض):

`sudo aa-unconfined`

- استفاده از `netstat` به جای `ss` برای تشخیص سوکت‌های شبکهٔ باز:

`sudo aa-unconfined --with-netstat`

- نمایش همهٔ فرایندهای `/proc` با درگاه‌های TCP/UDP و بدون پروفایل AppArmor (با جزئیات بیشتر):

`sudo aa-unconfined --paranoid`

- نمایش راهنما:

`aa-unconfined {{[-h|--help]}}`
