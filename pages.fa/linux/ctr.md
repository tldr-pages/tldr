# ctr

> مدیریت کانتینرها و تصاویر `containerd`.
> اطلاعات بیشتر: <https://manned.org/ctr>.

- فهرست کردن همهٔ کانتینرها (در حال اجرا و متوقف):

`ctr containers list`

- فهرست کردن همهٔ تصاویر:

`ctr images list`

- دریافت یک تصویر:

`ctr images pull {{image}}`

- برچسب‌گذاری یک تصویر:

`ctr images tag {{source_image}}:{{source_tag}} {{target_image}}:{{target_tag}}`
