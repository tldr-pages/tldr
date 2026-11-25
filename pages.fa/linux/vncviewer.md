# vncviewer

> اجرای کارخواه VNC (رایانش شبکه‌ای مجازی).
> اطلاعات بیشتر: <https://manned.org/vncviewer>.

- اجرای کارخواه VNC و اتصال به میزبان روی نمایشگر مشخص:

`vncviewer {{host}}:{{display_number}}`

- اجرا در حالت تمام‌صفحه:

`vncviewer -FullScreen {{host}}:{{display_number}}`

- اجرای کارخواه VNC با ابعاد مشخص صفحه:

`vncviewer --geometry {{width}}x{{height}} {{host}}:{{display_number}}`

- اجرای کارخواه VNC و اتصال به میزبان روی پورت مشخص:

`vncviewer {{host}}::{{port}}`
