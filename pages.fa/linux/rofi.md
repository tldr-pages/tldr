# rofi

> اجراکنندهٔ برنامه و تعویض‌کنندهٔ پنجره.
> اطلاعات بیشتر: <https://github.com/davatorium/rofi#manpage>.

- نمایش فهرست برنامه‌ها:

`rofi -show drun`

- نمایش فهرست همهٔ دستورها:

`rofi -show run`

- جابجایی بین پنجره‌ها:

`rofi -show window`

- ارسال فهرست موارد به `stdin` و چاپ مورد انتخاب‌شده در `stdout`:

`printf "{{Choice1\nChoice2\nChoice3}}" | rofi -dmenu`
