# flatpak history

> نمایش تاریخچهٔ تغییرات نصب‌های Flatpak در سیستم.
> همچنین ببینید: `journalctl`.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-history>.

- نمایش همهٔ موارد تاریخچهٔ Flatpak:

`flatpak history`

- نمایش موارد تاریخچهٔ کاربر فعلی به جای کل سیستم:

`flatpak history {{[-u|--user]}}`

- نمایش موارد تاریخچه از تاریخ یا زمان مشخص به بعد:

`flatpak history --since {{time}}`

- نمایش موارد تاریخچه تا تاریخ یا زمان مشخص:

`flatpak history --until {{time}}`

- نمایش موارد تاریخچه با جدیدترین تغییرات در ابتدا:

`flatpak history --reverse`

- نمایش ستون‌های اطلاعاتی مشخص:

`flatpak history --columns {{application,change,time,...}}`
