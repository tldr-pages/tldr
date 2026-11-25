# pw-metadata

> پایش، تنظیم و حذف فرادادهٔ اشیای PipeWire.
> همچنین : `pipewire`, `pw-mon`, `pw-cli`.
> اطلاعات بیشتر: <https://docs.pipewire.org/page_man_pw-metadata_1.html>.

- نمایش فراداده با نام `default`:

`pw-metadata`

- نمایش فراداده با شناسهٔ ۰ در `settings`:

`pw-metadata {{[-n|--name]}} settings 0`

- فهرست کردن همهٔ اشیای فرادادهٔ موجود:

`pw-metadata {{[-l|--list]}}`

- ادامهٔ اجرا و ثبت تغییرات فراداده:

`pw-metadata {{[-m|--monitor]}}`

- حذف همهٔ فراداده‌ها:

`pw-metadata {{[-d|--delete]}}`

- تنظیم `log.level` به ۱ در `settings`:

`pw-metadata {{[-n|--name]}} settings {{0}} log.level 1`

- نمایش راهنما:

`pw-metadata {{[-h|--help]}}`
