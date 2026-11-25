# konsave

> ذخیره و اعمال سفارشی‌سازی‌های لینوکس تنها با یک دستور.
> اطلاعات بیشتر: <https://github.com/Prayag2/konsave>.

- ذخیرهٔ پیکربندی فعلی به‌صورت پروفایل:

`konsave {{[-s|--save]}} {{profile_name}}`

- اعمال یک پروفایل:

`konsave {{[-a|--apply]}} {{profile_name}}`

- ذخیرهٔ پیکربندی فعلی به‌صورت پروفایل و بازنویسی پروفایل موجود در صورت هم‌نام بودن:

`konsave {{[-s|--save]}} {{profile_name}} {{[-f|--force]}}`

- فهرست کردن همهٔ پروفایل‌ها:

`konsave {{[-l|--list]}}`

- حذف پروفایل:

`konsave {{[-r|--remove]}} {{profile_name}}`

- صادر کردن پروفایل به‌صورت فایل `.knsv` در دایرکتوری خانگی:

`konsave {{[-e|--export-profile]}} {{profile_name}}`

- وارد کردن پروفایل `.knsv`:

`konsave {{[-i|--import-profile]}} {{path/to/profile_name.knsv}}`
