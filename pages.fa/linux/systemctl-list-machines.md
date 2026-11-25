# systemctl list-machines

> فهرست کردن میزبان و همهٔ ماشین‌های مجازی یا کانتینرهای محلی در حال اجرا همراه با وضعیت آن‌ها.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-machines%20PATTERN%E2%80%A6>.

- نمایش همهٔ ماشین‌ها (میزبان و کانتینرها یا ماشین‌های مجازی در حال اجرا):

`systemctl list-machines`

- فهرست کردن ماشین مشخص:

`systemctl list-machines {{machine}}`

- فهرست کردن چند ماشین مطابق:

`systemctl list-machines {{machine_1 machine_2 ...}}`

- فیلتر ماشین‌ها با الگوهای wildcard یعنی `glob`:

`systemctl list-machines {{pattern}}`
