# lvreduce

> کاهش اندازهٔ حجم منطقی.
> همچنین ببینید: `lvm`.
> اطلاعات بیشتر: <https://manned.org/lvreduce>.

- کاهش اندازهٔ حجم به ۱۲۰ گیگابایت:

`sudo lvreduce {{[-L|--size]}} {{120G}} {{logical_volume}}`

- کاهش اندازهٔ حجم و فایل‌سیستم زیرین آن به‌اندازهٔ ۴۰ گیگابایت:

`sudo lvreduce {{[-L|--size]}} -{{40G}} {{[-r|--resizefs]}} {{logical_volume}}`
