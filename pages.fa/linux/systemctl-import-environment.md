# systemctl import-environment

> وارد کردن متغیرهای محیطی از پوسته به محیط systemd.
> همچنین : `systemctl show-environment`, `systemctl unset-environment`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#import-environment%20VARIABLE%E2%80%A6>.

- وارد کردن متغیر:

`systemctl import-environment {{variable}}`

- وارد کردن چند متغیر:

`systemctl import-environment {{variable_1 variable_2 ...}}`

- وارد کردن متغیرها برای سرویس‌های کاربر:

`systemctl import-environment {{variable}} --user`
