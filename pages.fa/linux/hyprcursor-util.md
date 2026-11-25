# hyprcursor-util

> ابزار ایجاد و استخراج تم‌های نشانگر Hyprcursor برای Hyprland.
> اطلاعات بیشتر: <https://github.com/hyprwm/hyprcursor/blob/main/hyprcursor-util/README.md>.

- کامپایل یک دایرکتوری کاری به تم Hyprcursor:

`hyprcursor-util {{[-c|--create]}} {{path/to/theme_directory}}`

- استخراج تم XCursor در دایرکتوری کاری Hyprcursor:

`hyprcursor-util {{[-e|--extract]}} {{path/to/xcursor_theme}}`

- تعیین دایرکتوری خروجی:

`hyprcursor-util {{[-c|--create]}} {{path/to/theme_directory}} {{[-o|--output]}} {{path/to/output}}`

- استخراج تم با حالت تغییر اندازهٔ مشخص:

`hyprcursor-util --extract {{path/to/xcursor_theme}} --resize {{none|nearest|bilinear}}`
