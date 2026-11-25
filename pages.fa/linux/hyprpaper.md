# hyprpaper

> ابزار تصویر پس‌زمینهٔ Hyprland با امکان تغییر پویای تصاویر.
> توسط فایل پیکربندی `~/.config/hypr/hyprpaper.conf` کنترل می‌شود.
> اطلاعات بیشتر: <https://wiki.hypr.land/Hypr-Ecosystem/hyprpaper/>.

- شروع سرویس `hyprpaper`:

`hyprpaper`

- تغییر تصویر پس‌زمینهٔ نمایشگر مشخص:

`hyprctl hyprpaper wallpaper "{{monitor}},{{path/to/image.png}}"`

- تغییر تصویر پس‌زمینهٔ پیش‌فرض همهٔ نمایشگرهای مشخص‌نشده و تنظیم حالت تناسب آن:

`hyprctl hyprpaper wallpaper ",{{path/to/image.png}},{{contain|cover|tile|fill}}"`
