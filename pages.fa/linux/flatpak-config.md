# flatpak config

> مدیریت پیکربندی Flatpak.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-config>.

- فهرست کردن همهٔ تنظیمات پیکربندی:

`flatpak config --list`

- نمایش مقدار یک تنظیم پیکربندی مشخص:

`flatpak config --get {{key}}`

- تنظیم یک گزینهٔ پیکربندی:

`flatpak config --set {{key}} {{value}}`

- حذف یک گزینهٔ پیکربندی:

`flatpak config --unset {{key}}`

- فهرست کردن تنظیمات سراسری سیستم به جای تنظیمات کاربر:

`flatpak config --system --list`
