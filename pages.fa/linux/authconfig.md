# authconfig

> پیکربندی منابع احراز هویت سیستم.
> اطلاعات بیشتر: <https://manned.org/authconfig>.

- نمایش پیکربندی فعلی:

`authconfig --test`

- پیکربندی سرور برای استفاده از یک الگوریتم هش رمز عبور دیگر:

`authconfig --update --passalgo={{algorithm}}`

- فعال کردن احراز هویت LDAP:

`authconfig --update --enableldapauth`

- غیرفعال کردن احراز هویت LDAP:

`authconfig --update --disableldapauth`

- فعال کردن سرویس اطلاعات شبکه (NIS):

`authconfig --update --enablenis`

- فعال کردن Kerberos:

`authconfig --update --enablekrb5`

- فعال کردن احراز هویت Winbind (اکتیو دایرکتوری):

`authconfig --update --enablewinbindauth`

- فعال کردن مجوزدهی محلی:

`authconfig --update --enablelocauthorize`
