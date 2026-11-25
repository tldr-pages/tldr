# systemctl thaw

> خارج کردن یک یا چند واحد منجمد از انجماد (ادامهٔ اجرا).
> واحدها را می‌توان با `systemctl freeze` منجمد کرد.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#thaw%20PATTERN%E2%80%A6>.

- خارج کردن واحد مشخص از انجماد:

`systemctl thaw {{unit}}`

- خارج کردن چند واحد از انجماد:

`systemctl thaw {{unit1 unit2 ...}}`

- خارج کردن همهٔ واحدهای منجمد فعلی از انجماد:

`systemctl thaw '*'`
