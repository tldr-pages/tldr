# catimg

> چاپ عکس در ترمینال.
> موارد مشابه: `pixterm`, `chafa`.
> اطلاعات بیشتر: <https://github.com/posva/catimg>.

- چاپ یک JPEG, PNG, یا GIF در ترمینال:

`catimg {{path/to/file}}`

- دوبرابر کردن وضوح یک تصویر:

`catimg -r 2 {{path/to/file}}`

- غیرفعال سازی رنگ 24 بیتی برای پشتیبانی بهتر ترمینال:

`catimg -t {{path/to/file}}`

- مشخص کردن طول و عرض دلخواه:

`catimg {{-w|-H}} {{40}} {{path/to/file}}`
