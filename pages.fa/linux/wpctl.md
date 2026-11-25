# wpctl

> مدیریت WirePlumber، مدیر نشست و سیاست برای PipeWire.
> توجه: برای عمل روی خروجی پیش‌فرض می‌توانید از نام ویژهٔ `@DEFAULT_SINK@` به‌جای `id` استفاده کنید.
> همچنین ببینید: `pw-cli`.
> اطلاعات بیشتر: <https://pipewire.pages.freedesktop.org/wireplumber/>.

- فهرست کردن همهٔ اشیای مدیریت‌شده توسط WirePlumber:

`wpctl status`

- چاپ همهٔ ویژگی‌های یک شیء:

`wpctl inspect {{object_id}}`

- تنظیم شیء به‌عنوان پیش‌فرض گروه آن:

`wpctl set-default {{object_id}}`

- دریافت بلندی صدای یک خروجی:

`wpctl get-volume {{sink_id}}`

- تنظیم بلندی صدای خروجی به `n` درصد یا افزایش یا کاهش آن به اندازهٔ `n`:

`wpctl set-volume {{sink_id}} {{n%|n%+|n%-}}`

- فیلتر کردن اشیا بر اساس نوع:

`wpctl list {{audio|video}} {{devices|sinks|sources}}`

- افزایش بلندی صدای خروجی به اندازهٔ `n` درصد با محدود کردن صدا به کمتر از ۱۰۰٪:

`wpctl set-volume {{[-l|--limit]}} 1 {{sink_id}} {{n}}%-`

- قطع یا وصل صدای خروجی یا منبع صوتی پیش‌فرض (۱ برای قطع و ۰ برای وصل):

`wpctl set-mute @DEFAULT_{{SINK|SOURCE}}@ {{1|0|toggle}}`
