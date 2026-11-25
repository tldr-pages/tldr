# systemctl reset-failed

> بازنشانی وضعیت «شکست‌خورده» یک یا چند واحد.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#reset-failed%20%5BPATTERN%E2%80%A6%5D>.

- بازنشانی وضعیت شکست‌خوردهٔ همهٔ واحدها:

`systemctl reset-failed`

- بازنشانی وضعیت شکست‌خوردهٔ واحد مشخص:

`systemctl reset-failed {{unit}}`

- بازنشانی چند واحد هم‌زمان:

`systemctl reset-failed {{unit_1 unit_2 ...}}`
