# waypipe

> اجرای برنامه‌های گرافیکی از راه دور تحت compositor مربوط به Wayland.
> اطلاعات بیشتر: <https://manned.org/waypipe>.

- اجرای برنامهٔ گرافیکی از راه دور و نمایش محلی آن:

`waypipe ssh {{user}}@{{server}} {{program}}`

- باز کردن تونل SSH برای اجرای هر برنامه از راه دور و نمایش محلی آن:

`waypipe ssh {{user}}@{{server}}`

- صرف‌نظر از آزمون پشتیبانی Vulkan:

`waypipe --test-skip-vulkan ssh {{user}}@{{server}} {{program}}`

- نمایش راهنما:

`waypipe {{[-h|--help]}}`
