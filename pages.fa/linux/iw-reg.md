# iw reg

> مدیریت حوزه‌های مقرراتی WLAN.
> اطلاعات بیشتر: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- نمایش حوزهٔ مقرراتی فعلی:

`iw reg get`

- تنظیم حوزهٔ مقرراتی مطابق ISO 3166-1 alpha-2:

`sudo iw reg set {{US|JP|FI|...}}`

- بارگذاری مجدد پایگاه دادهٔ مقرراتی هسته:

`sudo iw reg reload`
