# hyprsunset

> فیلتر نور آبی برای Hyprland.
> در صورت تمایل از طریق `~/.config/hypr/hyprsunset.conf` پیکربندی می‌شود.
> اطلاعات بیشتر: <https://wiki.hypr.land/Hypr-Ecosystem/hyprsunset/>.

- شروع سرویس hyprsunset:

`hyprsunset`

- شروع سرویس hyprsunset با دمای رنگ و درصد گامای مشخص:

`hyprsunset {{[-t|--temperature]}} {{temperature}} {{[-g|--gamma]}} {{gamma}}`

- تنظیم دمای رنگ هنگام اجرای سرویس hyprsunset:

`hyprctl hyprsunset temperature {{temperature}}`

- تنظیم گاما هنگام اجرای سرویس hyprsunset:

`hyprctl hyprsunset gamma {{gamma}}`

- بازنشانی دمای رنگ به 6000K:

`hyprctl hyprsunset reset temperature`

- بازنشانی گاما به ۱۰۰ درصد:

`hyprctl hyprsunset reset gamma`
