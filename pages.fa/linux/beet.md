# beet

> مدیریت کتابخانهٔ رسانه‌ای beets.
> اطلاعات بیشتر: <https://beets.readthedocs.io/en/stable/reference/cli.html>.

- افزودن موسیقی از یک دایرکتوری مشخص به کتابخانه، با تلاش برای دریافت برچسب‌های صحیح از MusicBrainz:

`beet import {{path/to/directory}}`

- افزودن یک آهنگ به کتابخانه، با تلاش برای دریافت برچسب‌های صحیح از MusicBrainz:

`beet import {{[-s|--singletons]}} {{path/to/file}}`

- جست‌وجو در کتابخانه:

`beet list {{query}}`

- نمایش آمار کل کتابخانه:

`beet stats`

- نمایش آمار یک پرس‌وجوی مشخص:

`beet stats {{query}}`
