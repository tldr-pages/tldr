# wl-copy

> پاک کردن و کپی در کلیپ‌بورد Wayland.
> همچنین : `wl-paste`, `xclip`.
> اطلاعات بیشتر: <https://github.com/bugaevc/wl-clipboard>.

- کپی متن در کلیپ‌بورد:

`wl-copy "{{text}}"`

- هدایت خروجی دستور (`ls`) به کلیپ‌بورد:

`{{ls}} | wl-copy`

- کپی فقط برای یک بار چسباندن و سپس پاک کردن آن:

`wl-copy --paste-once "{{text}}"`

- کپی تصویر:

`wl-copy <{{path/to/image}}`

- پاک کردن کلیپ‌بورد:

`wl-copy --clear`
