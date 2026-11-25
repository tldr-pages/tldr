# wmctrl

> رابط خط فرمان برای مدیر پنجرهٔ X.
> اطلاعات بیشتر: <https://manned.org/wmctrl>.

- فهرست کردن همهٔ پنجره‌های مدیریت‌شده توسط مدیر پنجره:

`wmctrl -l`

- رفتن به نخستین پنجره‌ای که عنوان کامل یا بخشی از آن مطابقت دارد:

`wmctrl -a {{window_title}}`

- انتقال پنجره به فضای کاری فعلی، بالا آوردن و متمرکز کردن آن:

`wmctrl -R {{window_title}}`

- رفتن به فضای کاری:

`wmctrl -s {{workspace_number}}`

- انتخاب پنجره و تغییر وضعیت تمام‌صفحه:

`wmctrl -r {{window_title}} -b toggle,fullscreen`

- انتخاب پنجره و انتقال آن به فضای کاری:

`wmctrl -r {{window_title}} -t {{workspace_number}}`
