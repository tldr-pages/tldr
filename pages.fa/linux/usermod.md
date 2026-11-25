# usermod

> تغییر حساب کاربری.
> همچنین : `users`, `useradd`, `userdel`.
> اطلاعات بیشتر: <https://manned.org/usermod>.

- تغییر نام کاربری:

`sudo usermod {{[-l|--login]}} {{new_username}} {{username}}`

- تغییر شناسهٔ کاربر:

`sudo usermod {{[-u|--uid]}} {{user_id}} {{username}}`

- تغییر پوستهٔ کاربر:

`sudo usermod {{[-s|--shell]}} {{path/to/shell}} {{username}}`

- افزودن کاربر به گروه‌های تکمیلی (به نبود فاصله توجه کنید):

`sudo usermod {{[-aG|--append --groups]}} {{group1,group2,...}} {{username}}`

- حذف کاربر از گروه‌های مشخص:

`sudo usermod {{[-rG|--remove --groups]}} {{group1,group2,...}} {{username}}`

- تغییر دایرکتوری خانگی کاربر:

`sudo usermod {{[-m|--move-home]}} {{[-d|--home]}} {{path/to/new_home}} {{username}}`

- قفل کردن حساب:

`sudo usermod {{[-L|--lock]}} {{username}}`

- باز کردن قفل حساب:

`sudo usermod {{[-U|--unlock]}} {{username}}`
