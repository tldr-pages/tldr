# pw-dot

> ایجاد فایل‌های `.dot` از گراف PipeWire.
> همچنین : `dot`.
> اطلاعات بیشتر: <https://docs.pipewire.org/page_man_pw-dot_1.html>.

- تولید گراف در فایل `pw.dot`:

`pw-dot`

- خواندن اشیا از فایل JSON مربوط به `pw-dump`:

`pw-dot {{[-j|--json]}} {{path/to/file.json}}`

- تعیین فایل خروجی و نمایش همهٔ انواع اشیا:

`pw-dot {{[-o|--output]}} {{path/to/file.dot}} {{[-a|--all]}}`

- چاپ گراف `.dot` در `stdout` و نمایش همهٔ ویژگی‌های اشیا:

`pw-dot {{[-o|--output]}} - {{[-d|--detail]}}`

- تولید گراف از نمونهٔ راه دور با نمایش فقط اشیای پیوندشده:

`pw-dot {{[-r|--remote]}} {{remote_name}} {{[-s|--smart]}}`

- چیدمان گراف از چپ به راست به‌جای بالا به پایین پیش‌فرض dot:

`pw-dot {{[-L|--lr]}}`

- چیدمان گراف با زاویه‌های ۹۰ درجه در یال‌ها:

`pw-dot {{[-9|--90]}}`

- نمایش راهنما:

`pw-dot {{[-h|--help]}}`
