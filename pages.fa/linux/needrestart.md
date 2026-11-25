# needrestart

> بررسی سرویس‌هایی که پس از ارتقای کتابخانه‌ها باید مجدداً راه‌اندازی شوند.
> اطلاعات بیشتر: <https://manned.org/needrestart>.

- فهرست کردن فرایندهای قدیمی:

`needrestart`

- راه‌اندازی مجدد تعاملی سرویس‌ها:

`sudo needrestart`

- فهرست کردن فرایندهای قدیمی در حالت مفصل یا کم‌صدا:

`needrestart {{-v|-q}}`

- بررسی قدیمی بودن هسته:

`needrestart -k`

- بررسی قدیمی بودن ریزکد CPU:

`needrestart -w`

- فهرست کردن فرایندهای قدیمی در حالت دسته‌ای:

`needrestart -b`

- فهرست کردن فرایندهای قدیمی با فایل پیکربندی مشخص:

`needrestart -c {{path/to/config}}`

- نمایش راهنما:

`needrestart --help`
