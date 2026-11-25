# scrub

> بازنویسی امن فایل‌ها، دستگاه‌های بلوکی یا فضای آزاد دیسک.
> اطلاعات بیشتر: <https://manned.org/scrub>.

- بازنویسی امن فایل با الگوی پیش‌فرض:

`scrub {{path/to/file}}`

- بازنویسی امن چند فایل:

`scrub {{path/to/file1 path/to/file2 ...}}`

- بازنویسی امن دستگاه بلوکی یا پارتیشن:

`sudo scrub {{/dev/sdX}}`

- بازنویسی امن فایل با الگوی یک‌گذری:

`scrub {{[-p|--pattern]}} random {{path/to/file}}`

- بازنویسی امن فایل با الگوی DoD 5220.22-M:

`scrub {{[-p|--pattern]}} dod {{path/to/file}}`

- بازنویسی امن فایل با الگوی Gutmann:

`scrub {{[-p|--pattern]}} gutmann {{path/to/file}}`

- حذف فایل پس از بازنویسی موفق:

`scrub {{[-r|--remove]}} {{path/to/file}}`

- بازنویسی امن فضای آزاد در دایرکتوری:

`scrub {{[-X|--freespace]}} {{path/to/directory}}`
