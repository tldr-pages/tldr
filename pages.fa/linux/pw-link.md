# pw-link

> مدیریت پیوندهای بین پورت‌ها در PipeWire.
> اطلاعات بیشتر: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- فهرست کردن همهٔ پورت‌های ورودی و خروجی صوتی همراه با شناسه:

`pw-link {{[-oiI|--output --input --id]}}`

- ایجاد پیوند بین پورت خروجی و ورودی:

`pw-link {{output_port_name}} {{input_port_name}}`

- قطع اتصال دو پورت:

`pw-link {{[-d|--disconnect]}} {{output_port_name}} {{input_port_name}}`

- فهرست کردن همهٔ پیوندها همراه با شناسه:

`pw-link {{[-lI|--links --id]}}`

- نمایش راهنما:

`pw-link {{[-h|--help]}}`
