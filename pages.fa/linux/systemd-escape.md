# systemd-escape

> گریزگذاری رشته‌ها برای استفاده در نام واحدهای systemd.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-escape.html>.

- گریزگذاری متن مشخص:

`systemd-escape {{text}}`

- معکوس کردن فرایند گریزگذاری:

`systemd-escape {{[-u|--unescape]}} {{text}}`

- در نظر گرفتن متن مشخص به‌عنوان مسیر:

`systemd-escape {{[-p|--path]}} {{text}}`

- افزودن پسوند مشخص به متن گریزگذاری‌شده:

`systemd-escape --suffix {{suffix}} {{text}}`

- استفاده از قالب و تزریق متن گریزگذاری‌شده:

`systemd-escape --template {{template}} {{text}}`
