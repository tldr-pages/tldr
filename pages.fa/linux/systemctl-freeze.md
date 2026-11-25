# systemctl freeze

> منجمد کردن یک یا چند واحد.
> واحدهای منجمد را می‌توان با `systemctl thaw` ادامه داد.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#freeze%20PATTERN%E2%80%A6>.

- منجمد کردن واحد مشخص:

`systemctl freeze {{unit}}`

- منجمد کردن چند واحد:

`systemctl freeze {{unit1 unit2 ...}}`

- منجمد کردن همهٔ واحدهای در حال اجرا:

`systemctl freeze '*'`
