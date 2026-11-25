# fuzzel

> اجراکنندهٔ برنامه و جست‌وجوگر فازی بومی Wayland، الهام‌گرفته از `rofi` و `dmenu`.
> اطلاعات بیشتر: <https://codeberg.org/dnkl/fuzzel>.

- اجرای برنامه‌ها:

`fuzzel`

- اجرای `fuzzel` در حالت dmenu:

`fuzzel {{[-d|--dmenu]}}`

- نمایش منویی از خروجی دستور `ls`:

`{{ls}} | fuzzel {{[-d|--dmenu]}}`

- نمایش منو با موارد دلخواه جداشده با خط جدید (`\n`):

`echo -e "{{red}}\n{{green}}\n{{blue}}" | fuzzel {{[-d|--dmenu]}}`

- اجازه دادن به کاربر برای انتخاب از میان چند مورد و ذخیرهٔ مورد انتخاب‌شده در فایل:

`echo -e "{{red}}\n{{green}}\n{{blue}}" | fuzzel {{[-d|--dmenu]}} >{{color.txt}}`

- بازنشانی تعداد دفعات استفاده از برنامه‌ها (دایرکتوری پیش‌فرض حافظهٔ نهان: `$XDG_CACHE_HOME/fuzzel`):

`rm {{[-v|--verbose]}} $HOME/.cache/fuzzel`

- اجرای `fuzzel` روی نمایشگر مشخص؛ `wlr-randr` یا `swaymsg --type get_outputs` را ببینید:

`fuzzel {{[-o|--output]}} "{{DP-1}}"`

- استفاده از `fuzzel` برای جست‌وجوی اینترنتی:

`fuzzel {{[-d|--dmenu]}} {{[-l|--lines]}} 0 --placeholder "{{Type your search}}" | sed 's/^/\"/g;s/$/\"/g' | xargs firefox --search`
