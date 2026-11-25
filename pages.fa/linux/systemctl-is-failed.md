# systemctl is-failed

> بررسی شکست یک یا چند واحد systemd.
> همچنین ببینید: `systemctl is-active`, `systemctl status`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#is-failed%20PATTERN%E2%80%A6>.

- بررسی وجود واحدهای شکست‌خورده:

`systemctl is-failed`

- بررسی شکست یک یا چند واحد:

`systemctl is-failed {{unit1 unit2 ...}}`

- عدم نمایش خروجی و بازگرداندن فقط کد خروج:

`systemctl is-failed {{unit}} {{[-q|--quiet]}}`

- بررسی شکست واحد کاربر:

`systemctl is-failed {{unit}} --user`
