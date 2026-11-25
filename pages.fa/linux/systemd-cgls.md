# systemd-cgls

> نمایش محتویات سلسله‌مراتب گروه کنترل انتخاب‌شدهٔ لینوکس به‌صورت درختی.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-cgls.html>.

- نمایش کل سلسله‌مراتب گروه کنترل در سیستم:

`systemd-cgls`

- نمایش درخت گروه کنترل کنترل‌کنندهٔ منبع مشخص:

`systemd-cgls {{cpu|memory|io}}`

- نمایش سلسله‌مراتب گروه کنترل یک یا چند واحد systemd:

`systemd-cgls {{[-u|--unit]}} {{unit1 unit2 ...}}`
