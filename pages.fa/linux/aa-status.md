# aa-status

> فهرست کردن ماژول‌های AppArmor که در حال حاضر بارگذاری شده‌اند.
> همچنین ببینید: `aa-complain`, `aa-disable`, `aa-enforce`.
> اطلاعات بیشتر: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>.

- بررسی وضعیت:

`sudo aa-status`

- نمایش وضعیت در قالب JSON:

`sudo aa-status --json`

- نمایش وضعیت در قالب JSON خوانا:

`sudo aa-status --pretty-json`

- نمایش تعداد سیاست‌های بارگذاری‌شده:

`sudo aa-status --profiled`

- نمایش تعداد سیاست‌های بارگذاری‌شده در حالت اعمال اجباری:

`sudo aa-status --enforced`

- نمایش تعداد سیاست‌های بارگذاری‌شده خارج از حالت اعمال اجباری:

`sudo aa-status --complaining`

- نمایش تعداد سیاست‌های بارگذاری‌شده در حالت اعمال اجباری که وظایف را خاتمه می‌دهند:

`sudo aa-status --kill`
