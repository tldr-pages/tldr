# you-get

> دانلود محتوای چندرسانه ای از وب (ویدیو، صوت، عکس).
> همچنین : `yt-dlp`, `youtube-viewer`, `instaloader`.
> اطلاعات بیشتر: <https://you-get.org/#getting-started>.

- چاپ اطلاعات درمورد یک رسانه خاص در سطح وب:

`you-get {{[-i|--info]}} {{https://example.com/video?id=value}}`

- دانلود رسانه از لینک موردنظر:

`you-get {{https://example.com/video?id=value}}`

- جستجو در ویدیوهای گوگل و دانلود:

`you-get {{keywords}}`

- دانلود یک رسانه و ذخیره در محل ذخیره شده:

`you-get {{[-o|--output-dir]}} {{path/to/directory}} {{[-O|--output-filename]}} {{filename}} {{https://example.com/watch?v=value}}`

- دانلود یک رسانه با استفاده از پروکسی:

`you-get {{[-x|--http-proxy]}} {{proxy_server}} {{https://example.com/watch?v=value}}`
