# lvresize

> تغییر اندازهٔ حجم منطقی.
> همچنین : `lvm`.
> اطلاعات بیشتر: <https://manned.org/lvresize>.

- تغییر اندازهٔ حجم منطقی به ۱۲۰ گیگابایت:

`sudo lvresize {{[-L|--size]}} 120G {{volume_group}}/{{logical_volume}}`

- افزایش اندازهٔ حجم منطقی و فایل‌سیستم زیرین آن به‌اندازهٔ ۱۲۰ گیگابایت:

`sudo lvresize {{[-L|--size]}} +120G {{[-r|--resizefs]}} {{volume_group}}/{{logical_volume}}`

- افزایش اندازهٔ حجم منطقی به ۱۰۰٪ فضای آزاد حجم فیزیکی:

`sudo lvresize {{[-l|--extents]}} 100%FREE {{volume_group}}/{{logical_volume}}`

- کاهش اندازهٔ حجم منطقی و فایل‌سیستم زیرین آن به‌اندازهٔ ۱۲۰ گیگابایت:

`sudo lvresize {{[-L|--size]}} -120G {{[-r|--resizefs]}} {{volume_group}}/{{logical_volume}}`
