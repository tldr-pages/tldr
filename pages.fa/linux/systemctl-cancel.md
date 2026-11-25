# systemctl cancel

> لغو یک یا چند کار در انتظار در مدیر سیستم یا مدیر کاربر.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#cancel%20JOB%E2%80%A6>.

- لغو کار با شناسهٔ عددی آن:

`systemctl cancel {{job_id}}`

- لغو چند کار:

`systemctl cancel {{job_id1 job_id2 ...}}`

- لغو همهٔ کارهای در انتظار:

`systemctl cancel`

- لغو کار در مدیر سرویس کاربر:

`systemctl cancel {{job_id}} --user`
