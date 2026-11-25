# walker

> اجراکنندهٔ برنامهٔ بومی Wayland با ارائه‌دهنده‌های قابل اتصال.
> همچنین : `fuzzel`, `wofi`, `rofi`.
> اطلاعات بیشتر: <https://github.com/abenz1267/walker>.

- باز کردن اجراکننده:

`walker`

- محدود کردن اجراکننده به یک ارائه‌دهنده:

`walker {{[-m|--provider]}} {{desktopapplications|calc|clipboard|runner|...}}`

- خواندن موارد از `stdin` و چاپ مورد انتخاب‌شده در `stdout` (حالت dmenu):

`printf "{{Choice1\nChoice2\nChoice3}}" | walker {{[-d|--dmenu]}}`

- باز کردن اجراکننده با پوستهٔ مشخص:

`walker {{[-t|--theme]}} {{theme_name}}`
