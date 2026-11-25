# pw-config

> فهرست کردن مسیرها و بخش‌های پیکربندی که توسط سرور و کارخواه‌های PipeWire استفاده خواهند شد.
> اطلاعات بیشتر: <https://docs.pipewire.org/page_man_pw-config_1.html>.

- فهرست کردن همهٔ فایل‌های پیکربندی مورد استفاده:

`pw-config`

- فهرست کردن همهٔ فایل‌های پیکربندی مورد استفادهٔ سرور PulseAudio مربوط به PipeWire:

`pw-config {{[-n|--name]}} pipewire-pulse.conf`

- فهرست کردن همهٔ بخش‌های پیکربندی مورد استفادهٔ سرور PulseAudio مربوط به PipeWire:

`pw-config {{[-n|--name]}} pipewire-pulse.conf list`

- فهرست کردن قطعه‌های `context.properties` مورد استفادهٔ کارخواه‌های JACK:

`pw-config {{[-n|--name]}} jack.conf list context.properties`

- فهرست کردن `context.properties` ادغام‌شدهٔ مورد استفادهٔ کارخواه‌های JACK:

`pw-config {{[-n|--name]}} jack.conf merge context.properties`

- فهرست کردن `context.modules` ادغام‌شدهٔ مورد استفادهٔ سرور PipeWire و قالب‌بندی مجدد:

`pw-config {{[-n|--name]}} pipewire.conf {{[-r|--recurse]}} merge context.modules`

- نمایش راهنما:

`pw-config {{[-h|--help]}}`
