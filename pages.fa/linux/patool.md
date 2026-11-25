# patool

> مدیر فایل‌های بایگانی.
> قالب‌های مختلف بایگانی را می‌توان ایجاد، استخراج، آزمایش، فهرست، جست‌وجو، بازبسته‌بندی و مقایسه کرد.
> اطلاعات بیشتر: <https://github.com/wummel/patool/blob/master/doc/patool.txt>.

- استخراج بایگانی:

`patool extract {{path/to/archive}}`

- ایجاد بایگانی:

`patool create {{path/to/archive}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- فهرست کردن محتویات بایگانی:

`patool list {{path/to/archive}}`

- مقایسهٔ محتویات دو بایگانی و نمایش تفاوت‌ها در `stdout`:

`patool diff {{path/to/archive1}} {{path/to/archive2}}`

- جست‌وجوی رشته در محتویات بایگانی:

`patool search {{path/to/archive}}`
