# pw-container

> اجرای برنامه در زمینهٔ امنیتی جدید.
> اطلاعات بیشتر: <https://docs.pipewire.org/page_man_pw-container_1.html>.

- ایجاد زمینهٔ امنیتی جدید و چاپ آدرس سوکت آن در `stdout`:

`pw-container`

- اجرای برنامهٔ مشخص در زمینهٔ امنیتی جدید:

`pw-container {{command}} {{argument1 argument2 ...}}`

- اجرای برنامه با اتصال به نمونهٔ راه دور مشخص PipeWire:

`pw-container {{[-r|--remote]}} {{remote_instance_name}} {{command}}`

- اجرای برنامه در زمینهٔ جدید با ویژگی‌های مشخص به‌صورت شیء JSON:

`pw-container {{[-P|--properties]}} '{{{"key": "value"}}}' {{command}}`

- نمایش راهنما:

`pw-container {{[-h|--help]}}`
