# pw-dump

> چاپ وضعیت فعلی PipeWire به‌صورت JSON، شامل اطلاعات گره‌ها، دستگاه‌ها، ماژول‌ها، پورت‌ها و سایر اشیا.
> همچنین ببینید: `pw-mon`.
> اطلاعات بیشتر: <https://docs.pipewire.org/page_man_pw-dump_1.html>.

- چاپ نمایش JSON وضعیت فعلی نمونهٔ پیش‌فرض PipeWire:

`pw-dump`

- چاپ نمایش JSON یک شیء:

`pw-dump {{object_id}}`

- چاپ وضعیت فعلی همراه با پایش تغییرات و چاپ دوبارهٔ آن:

`pw-dump {{[-m|--monitor]}}`

- ذخیرهٔ وضعیت فعلی نمونهٔ راه دور در فایل:

`pw-dump {{[-r|--remote]}} {{remote_name}} >{{path/to/dump_file.json}}`

- تنظیم پیکربندی رنگ:

`pw-dump {{[-C|--color]}} {{never|always|auto}}`

- نمایش راهنما:

`pw-dump {{[-h|--help]}}`
