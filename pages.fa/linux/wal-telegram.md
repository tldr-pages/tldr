# wal-telegram

> تولید پوسته برای Telegram بر اساس رنگ‌های تولیدشده توسط pywal/wal.
> اطلاعات بیشتر: <https://github.com/guillaumeboehm/wal-telegram>.

- تولید با پالت wal و تصویر زمینهٔ فعلی (فقط feh):

`wal-telegram`

- تولید با پالت wal و تصویر زمینهٔ مشخص:

`wal-telegram --background={{path/to/image}}`

- تولید با پالت wal و پس‌زمینهٔ رنگی بر اساس پالت:

`wal-telegram --tiled`

- اعمال محوشدگی گاوسی به تصویر زمینه:

`wal-telegram -g`

- تعیین محل پوستهٔ تولیدشده (پیش‌فرض `$XDG_CACHE_HOME/wal-telegram` یا `~/.cache/wal-telegram`):

`wal-telegram --destination={{path/to/destination}}`

- راه‌اندازی مجدد برنامهٔ telegram پس از تولید:

`wal-telegram --restart`
