# setterm

> تنظیم ویژگی‌های ترمینال مانند رنگ، نمایش مکان‌نما و خاموش شدن صفحه.
> توجه: برخی گزینه‌ها فقط در کنسول‌های مجازی (TTY) کار می‌کنند.
> اطلاعات بیشتر: <https://manned.org/setterm>.

- پاک کردن صفحه:

`setterm --clear`

- نمایان یا پنهان کردن مکان‌نما:

`setterm --cursor {{on|off}}`

- روشن یا خاموش کردن متن چشمک‌زن:

`setterm --blink {{on|off}}`

- تنظیم رنگ متن:

`setterm --foreground {{default|black|blue|red|...}}`

- تنظیم رنگ پس‌زمینه:

`setterm --background {{default|black|blue|red|...}}`

- تنظیم مهلت خاموش شدن صفحه بر حسب دقیقه (`0` آن را غیرفعال می‌کند):

`setterm --blank {{0..60}}`

- بازنشانی ترمینال به وضعیت پیش‌فرض:

`setterm --reset`
