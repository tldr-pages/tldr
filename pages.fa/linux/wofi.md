# wofi

> اجراکنندهٔ برنامه برای compositorهای Wayland مبتنی بر wlroots، مشابه `rofi` و `dmenu`.
> اطلاعات بیشتر: <https://manned.org/wofi>.

- نمایش فهرست برنامه‌ها:

`wofi {{[-S|--show]}} drun`

- نمایش فهرست همهٔ دستورها:

`wofi {{[-S|--show]}} run`

- هدایت فهرستی از موارد به `stdin` و چاپ مورد انتخاب‌شده در `stdout`:

`printf "{{Choice1\nChoice2\nChoice3}}" | wofi {{[-d|--dmenu]}}`
