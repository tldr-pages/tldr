# screenkey

> ابزار ضبط صفحه برای نمایش کلیدهای فشرده‌شده.
> اطلاعات بیشتر: <https://www.thregr.org/wavexx/software/screenkey/>.

- نمایش کلیدهایی که اکنون روی صفحه فشرده می‌شوند:

`screenkey`

- نمایش کلیدها و دکمه‌های ماوسی که اکنون روی صفحه فشرده می‌شوند:

`screenkey {{[-M|--mouse]}}`

- اجرای منوی تنظیمات screenkey:

`screenkey --show-settings`

- اجرای screenkey در موقعیت مشخص:

`screenkey {{[-p|--position]}} {{top|center|bottom|fixed}}`

- تغییر قالب کلیدهای تغییردهندهٔ نمایش‌داده‌شده روی صفحه:

`screenkey --mods-mode {{normal|emacs|mac|win|tux}}`

- تغییر ظاهر screenkey:

`screenkey --bg-color "{{#a1b2c3}}" {{[-f|--font]}} {{Hack}} --font-color {{yellow}} --opacity {{0.8}}`

- کشیدن و انتخاب پنجره‌ای روی صفحه برای نمایش screenkey:

`screenkey {{[-p|--position]}} fixed {{[-g|--geometry]}} {{$(slop --nodecorations --format '%g')}}`
