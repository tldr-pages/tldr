# run0

> افزایش تعاملی دسترسی‌ها.
> مشابه `sudo` است، اما فایل دودویی SUID نیست، احراز هویت از طریق polkit انجام می‌شود و دستورها از سرویس `systemd` فراخوانی می‌شوند.
> همچنین : `sudo`, `pkexec`, `doas`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/run0.html>.

- اجرای دستور با دسترسی root:

`run0 {{command}}`

- اجرای دستور به‌عنوان کاربر و یا گروه دیگر:

`run0 {{[-u|--user]}} {{username|user_id}} {{[-g|--group]}} {{group_name|group_id}} {{command}}`
