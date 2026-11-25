# protontricks

> واسط ساده‌ای که دستورهای Winetricks را برای بازی‌های پشتیبانی‌شده توسط Proton اجرا می‌کند.
> اطلاعات بیشتر: <https://github.com/Matoking/protontricks#usage>.

- اجرای رابط گرافیکی protontricks:

`protontricks --gui`

- اجرای Winetricks برای بازی مشخص:

`protontricks {{appid}} {{winetricks_args}}`

- اجرای دستور داخل دایرکتوری نصب بازی:

`protontricks {{[-c|--command]}} {{command}} {{appid}}`

- فهرست کردن همهٔ بازی‌های نصب‌شده:

`protontricks {{[-l|--list]}}`

- جست‌وجوی شناسهٔ برنامهٔ بازی با نام:

`protontricks {{[-s|--search]}} {{game_name}}`

- اجرای فایل اجرایی در محیط proton بازی مشخص:

`protontricks-launch --appid {{appid}} {{path/to/executable.exe}}`

- نمایش راهنما:

`protontricks {{[-h|--help]}}`
