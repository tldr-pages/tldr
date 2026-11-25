# distrobox-enter

> ورود به یک کانتینر Distrobox.
> دستور پیش‌فرض اجراشده `$SHELL` شما است، اما می‌توانید پوسته‌های دیگر یا دستورهای کامل را برای اجرا مشخص کنید. در اسکریپت، برنامه یا سرویس می‌توانید از حالت `--headless` برای غیرفعال کردن tty و تعامل استفاده کنید.
> همچنین : `distrobox`.
> اطلاعات بیشتر: <https://distrobox.it/usage/distrobox-enter/>.

- ورود به یک کانتینر Distrobox:

`distrobox-enter {{container_name}}`

- ورود به یک کانتینر Distrobox و اجرای دستور هنگام ورود:

`distrobox-enter {{container_name}} -- {{sh -l}}`

- ورود به یک کانتینر Distrobox بدون ایجاد tty:

`distrobox-enter {{[-n|--name]}} {{container_name}} -- {{uptime --pretty}}`
