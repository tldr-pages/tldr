# aa-decode

> رمزگشایی گزارش‌های ممیزی AppArmor به قالبی خوانا برای انسان.
> اطلاعات بیشتر: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-decode.8>.

- رمزگشایی یک رشتهٔ شانزده‌شانزدهی:

`aa-decode {{hexstring}}`

- رمزگشایی یک فایل گزارش:

`sudo aa-decode {{logfile}}`

- رمزگشایی گزارش‌ها از ورودی استاندارد `stdin` (برای مثال، فایل هدایت‌شده):

`sudo aa-decode - <{{logfile}}`

- نمایش راهنما:

`aa-decode {{[-h|--help]}}`
