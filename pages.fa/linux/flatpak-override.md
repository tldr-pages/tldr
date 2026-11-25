# flatpak override

> تغییر مجوزهای زمان اجرای برنامه‌های Flatpak.
> توجه: بدون `--user` نصب سراسری پیش‌فرض تغییر می‌کند. بدون مشخص کردن برنامه، تغییر روی همهٔ برنامه‌ها اعمال می‌شود.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-override>.

- نمایش تغییرات مجوز یک برنامه:

`flatpak override --show {{com.example.app}}`

- اعطای دسترسی یک برنامه به محلی در سیستم فایل:

`flatpak override --filesystem {{home|host|xdg-download|path/to/directory}} {{com.example.app}}`

- اعطای دسترسی فقط‌خواندنی یک برنامه به دایرکتوری:

`flatpak override --filesystem {{path/to/directory}}:ro {{com.example.app}}`

- توقف اشتراک شبکه با یک برنامه:

`flatpak override --unshare network {{com.example.app}}`

- تنظیم یک متغیر محیطی برای برنامه:

`flatpak override --env {{VARIABLE}}={{value}} {{com.example.app}}`

- اعمال تغییر فقط برای کاربر فعلی:

`flatpak override {{[-u|--user]}} --nosocket {{wayland}} {{com.example.app}}`

- حذف همهٔ تغییرات مجوز یک برنامه:

`flatpak override --reset {{com.example.app}}`
