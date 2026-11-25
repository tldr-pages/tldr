# edquota

> ویرایش سهمیه‌های یک کاربر یا گروه؛ به‌صورت پیش‌فرض روی همهٔ سیستم‌های فایل دارای سهمیه عمل می‌کند.
> اطلاعات سهمیه به‌طور دائمی در فایل‌های `quota.user` و `quota.group` در ریشهٔ سیستم فایل ذخیره می‌شود.
> اطلاعات بیشتر: <https://manned.org/edquota>.

- ویرایش سهمیهٔ کاربر فعلی:

`edquota {{[-u|--user]}} $(whoami)`

- ویرایش سهمیهٔ یک کاربر مشخص:

`sudo edquota {{[-u|--user]}} {{username}}`

- ویرایش سهمیهٔ یک گروه:

`sudo edquota {{[-g|--group]}} {{group}}`

- محدود کردن عملیات به سیستم فایل مشخص (به‌صورت پیش‌فرض edquota روی همهٔ سیستم‌های فایل دارای سهمیه عمل می‌کند):

`sudo edquota {{[-f|--file-system]}} {{filesystem}}`

- ویرایش مهلت ارفاقی پیش‌فرض:

`sudo edquota {{[-t|--edit-period]}}`

- کپی کردن سهمیه برای کاربران دیگر:

`sudo edquota {{[-p|--prototype]}} {{reference_user}} {{destination_user1 destination_user2 ...}}`
