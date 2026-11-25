# wireplumber

> مدیر ماژولار نشست و سیاست برای PipeWire و کتابخانهٔ سطح‌بالای مبتنی بر GObject که API مربوط به PipeWire را دربر می‌گیرد.
> همچنین ببینید: `wpctl`, `pipewire`.
> اطلاعات بیشتر: <https://pipewire.pages.freedesktop.org/wireplumber/>.

- شروع فوری WirePlumber همراه نشست کاربر (برای سیستم‌های systemd):

`systemctl enable wireplumber --user --now`

- اجرای WirePlumber پس از شروع `pipewire` (برای سیستم‌های بدون systemd):

`wireplumber`

- تعیین فایل پیکربندی context متفاوت:

`wireplumber {{[-c|--config-file]}} {{path/to/file}}`

- نمایش راهنما:

`wireplumber {{[-h|--help]}}`

- نمایش نسخه:

`wireplumber {{[-v|--version]}}`
