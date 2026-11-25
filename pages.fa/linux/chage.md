# chage

> تغییر اطلاعات انقضای حساب کاربری و رمز عبور.
> اطلاعات بیشتر: <https://manned.org/chage>.

- فهرست کردن اطلاعات رمز عبور کاربر:

`chage {{[-l|--list]}} {{username}}`

- فعال کردن انقضای رمز عبور پس از ۱۰ روز:

`sudo chage {{[-M|--maxdays]}} 10 {{username}}`

- غیرفعال کردن انقضای رمز عبور:

`sudo chage {{[-M|--maxdays]}} -1 {{username}}`

- تنظیم تاریخ انقضای حساب:

`sudo chage {{[-E|--expiredate]}} {{YYYY-MM-DD}} {{username}}`

- مجبور کردن کاربر به تغییر رمز عبور در ورود بعدی:

`sudo chage {{[-d|--lastday]}} 0 {{username}}`

- فعال کردن مجدد یک حساب:

`sudo chage {{[-E|--expiredate]}} -1 {{username}}`
