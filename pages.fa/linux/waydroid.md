# waydroid

> راهکاری مبتنی بر کانتینر برای راه‌اندازی سیستم کامل Android روی سیستم معمولی لینوکس مانند Ubuntu.
> اطلاعات بیشتر: <https://docs.waydro.id/usage/waydroid-command-line-options>.

- شروع Waydroid:

`waydroid show-full-ui`

- مقداردهی اولیهٔ Waydroid (در اجرای اول یا پس از نصب مجدد Android لازم است):

`sudo waydroid init`

- بررسی وضعیت کانتینر:

`waydroid status`

- نصب برنامهٔ Android جدید از فایل:

`waydroid app install {{path/to/file}}.apk`

- شروع یا توقف نشست Waydroid:

`waydroid session {{start|stop}}`

- مدیریت کانتینر Waydroid:

`sudo waydroid container {{start|stop|restart|freeze|unfreeze}}`

- باز کردن پوستهٔ Waydroid:

`sudo waydroid shell`

- تنظیم ابعاد پنجرهٔ Waydroid:

`waydroid prop set persist.waydroid.{{width|height}} {{number}}`
