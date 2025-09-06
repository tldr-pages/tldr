# you-get

> دانلود محتوای چندرسانه ای از وب (ویدیو، صوت، عکس).
> اطلاعات بیشتر: <https://you-get.org>.

- چاپ اطلاعات درمورد یک رسانه خاص در سطح وب:

`you-get --info {{https://example.com/video?id=value}}`

- دانلود رسانه از لینک موردنظر:

`you-get {{https://example.com/video?id=value}}`

- جستجو در ویدیوهای گوگل و دانلود:

`you-get {{keywords}}`

- دانلود یک رسانه و ذخیره در محل ذخیره شده:

`you-get --output-dir {{path/to/directory}} --output-filename {{filename}} {{https://example.com/watch?v=value}}`

- دانلود یک رسانه با استفاده از پروکسی:

`you-get --http-proxy {{proxy_server}} {{https://example.com/watch?v=value}}`
