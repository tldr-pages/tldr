# pacman-mirrors

> تولید فهرست آینهٔ `pacman` برای Manjaro Linux.
> هر بار اجرای `pacman-mirrors` نیازمند همگام‌سازی پایگاه داده و به‌روزرسانی سیستم با `sudo pacman -Syyu` است.
> همچنین : `pacman`.
> اطلاعات بیشتر: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- تولید فهرست آینه با تنظیمات پیش‌فرض:

`sudo pacman-mirrors --fasttrack`

- دریافت وضعیت آینه‌های فعلی:

`pacman-mirrors --status`

- نمایش شاخهٔ فعلی:

`pacman-mirrors --get-branch`

- تغییر به شاخهٔ دیگر:

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- فهرست کردن کشورهای موجود:

`pacman-mirrors --country-list`

- تولید فهرست آینه فقط با آینه‌های کشورهای مشخص:

`sudo pacman-mirrors --country {{United_States,France,Germany,...}}`
