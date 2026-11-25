# lvextend

> افزایش اندازهٔ حجم منطقی.
> همچنین : `lvm`.
> اطلاعات بیشتر: <https://manned.org/lvextend>.

- افزایش اندازهٔ حجم به ۱۲۰ گیگابایت:

`sudo lvextend {{[-L|--size]}} 120G {{logical_volume}}`

- افزایش اندازهٔ حجم و فایل‌سیستم زیرین آن به‌اندازهٔ ۴۰ گیگابایت:

`sudo lvextend {{[-L|--size]}} +40G {{[-r|--resizefs]}} {{logical_volume}}`

- افزایش اندازهٔ حجم به ۱۰۰٪ فضای آزاد حجم فیزیکی:

`sudo lvextend {{[-l|--extents]}} +100%FREE {{logical_volume}}`

- افزایش اندازهٔ حجم به ۱۰۰٪ فضای آزاد حجم فیزیکی و تغییر اندازهٔ فایل‌سیستم زیرین:

`sudo lvextend {{[-l|--extents]}} +100%FREE {{[-r|--resizefs]}} {{logical_volume}}`
