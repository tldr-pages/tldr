# speedread

> تندخوانی مشابه Spritz.
> نمایش متن با ارائهٔ بصری سریع و پیاپی واژه‌ها (RSVP).
> اطلاعات بیشتر: <https://github.com/pasky/speedread>.

- خواندن فایل متنی با سرعت مشخص:

`cat {{path/to/file.txt}} | speedread -wpm {{250}}`

- ادامه از خط مشخص:

`cat {{path/to/file.txt}} | speedread -resume {{5}}`

- نمایش چند واژه در هر بار:

`cat {{path/to/file.txt}} | speedread -multiword`

- کاهش سرعت به میزان ۱۰٪ هنگام خواندن:

`<[>`

- افزایش سرعت به میزان ۱۰٪ هنگام خواندن:

`<]>`

- توقف موقت و نمایش چند خط آخر به‌عنوان زمینه:

`<Space>`
