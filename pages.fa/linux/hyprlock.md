# hyprlock

> قفل‌کنندهٔ صفحه با شتاب‌دهی GPU برای ترکیب‌گر Wayland به نام Hyprland.
> از طریق `~/.config/hypr/hyprlock.conf` پیکربندی می‌شود.
> اطلاعات بیشتر: <https://wiki.hypr.land/Hypr-Ecosystem/hyprlock/>.

- قفل کردن صفحه با پیکربندی پیش‌فرض:

`hyprlock`

- قفل کردن صفحه با فایل پیکربندی مشخص:

`hyprlock {{[-c|--config]}} {{path/to/hyprlock.conf}}`

- قفل فوری صفحه بدون در نظر گرفتن مهلت ارفاقی:

`hyprlock --grace 0`

- غیرفعال کردن پویانمایی محوشدگی هنگام قفل:

`hyprlock --no-fade-in`

- نمایش راهنما:

`hyprlock {{[-h|--help]}}`
