# startx

> رابطی برای `xinit` که رابط کاربری مناسبی برای اجرای یک نشست X Window System فراهم می‌کند.
> اطلاعات بیشتر: <https://www.x.org/releases/X11R7.6/doc/man/man1/startx.1.xhtml>.

- شروع نشست X:

`startx`

- شروع نشست X با مقدار عمق ازپیش‌تعیین‌شده:

`startx -- -depth {{value}}`

- شروع نشست X با مقدار dpi ازپیش‌تعیین‌شده:

`startx -- -dpi {{value}}`

- نادیده گرفتن تنظیمات فایل `.xinitrc` و شروع نشست جدید X:

`startx /{{path/to/window_manager_or_desktop_environment}}`
