# systemctl restart

> توقف و سپس شروع یک یا چند واحد systemd.
> می‌توان آن را به‌جای `systemctl start` روی واحد متوقف‌شده استفاده کرد، اما `start` امن‌تر است تا واحد در حال اجرا اتفاقی راه‌اندازی مجدد نشود.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#restart%20PATTERN%E2%80%A6>.

- راه‌اندازی مجدد واحد:

`systemctl restart {{unit}}`

- راه‌اندازی مجدد بیش از یک واحد:

`systemctl restart {{unit1 unit2 ...}}`

- راه‌اندازی مجدد واحد کاربر:

`systemctl restart {{unit}} --user`
