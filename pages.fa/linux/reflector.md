# reflector

> اسکریپت Arch برای دریافت و مرتب‌سازی فهرست آینه‌ها.
> اطلاعات بیشتر: <https://manned.org/reflector>.

- دریافت همهٔ آینه‌ها، مرتب‌سازی بر اساس سرعت بارگیری و ذخیرهٔ آن‌ها:

`sudo reflector --sort {{rate}} --save {{/etc/pacman.d/mirrorlist}}`

- دریافت فقط آینه‌های HTTPS آلمان:

`reflector {{[-c|--country]}} Germany {{[-p|--protocol]}} https`

- دریافت فقط ۱۰ آینهٔ اخیراً همگام‌شده:

`reflector {{[-l|--latest]}} 10`

- استفاده از فایل پیکربندی برای دریافت آینه‌ها:

`sudo reflector @{{/etc/xdg/reflector/reflector.conf}}`

- نمایش راهنما:

`reflector {{[-h|--help]}}`
