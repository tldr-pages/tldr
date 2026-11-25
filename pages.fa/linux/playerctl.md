# playerctl

> کنترل پخش‌کننده‌های رسانه از طریق MPRIS.
> اطلاعات بیشتر: <https://github.com/altdesktop/playerctl#using-the-cli>.

- تغییر وضعیت پخش:

`playerctl play-pause`

- رفتن به ترک بعدی:

`playerctl next`

- بازگشت به ترک قبلی:

`playerctl previous`

- فهرست کردن همهٔ پخش‌کننده‌ها:

`playerctl {{[-l|--list-all]}}`

- ارسال دستور به پخش‌کنندهٔ مشخص:

`playerctl {{[-p|--player]}} {{player_name}} {{play-pause|next|previous|...}}`

- ارسال دستور به همهٔ پخش‌کننده‌ها:

`playerctl {{[-a|--all-players]}} {{play-pause|next|previous|...}}`

- نمایش فرادادهٔ ترک فعلی:

`playerctl metadata {{[-f|--format]}} "{{Now playing: \{\{artist\}\} - \{\{album\}\} - \{\{title\}\}}}"`
