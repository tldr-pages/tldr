# hyprctl

> کنترل بخش‌هایی از ترکیب‌گر Wayland به نام Hyprland.
> اطلاعات بیشتر: <https://wiki.hypr.land/Configuring/Advanced-and-Cool/Using-hyprctl/>.

- بارگذاری مجدد پیکربندی Hyprland:

`hyprctl reload`

- دریافت نام پنجرهٔ فعال:

`hyprctl activewindow`

- فهرست کردن همهٔ دستگاه‌های ورودی متصل:

`hyprctl devices`

- فهرست کردن همهٔ خروجی‌ها همراه با ویژگی‌های آن‌ها:

`hyprctl workspaces`

- فراخوانی یک dispatcher:

`hyprctl dispatch {{dispatcher}}`

- تنظیم پویای کلیدواژهٔ پیکربندی:

`hyprctl keyword {{keyword}} {{value}}`

- نمایش نسخه:

`hyprctl version`
