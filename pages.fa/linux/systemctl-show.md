# systemctl show

> نمایش ویژگی‌های واحدها یا خود systemd.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#show%20PATTERN%E2%80%A6%7CJOB%E2%80%A6>.

- نمایش ویژگی‌های مدیر سرویس سیستم:

`systemctl show`

- نمایش ویژگی‌های مدیر سرویس کاربر:

`systemctl show --user`

- نمایش ویژگی‌های واحد مشخص:

`systemctl show {{unit}}`

- نمایش ویژگی‌های واحد کاربر مشخص:

`systemctl show {{unit}} --user`

- گنجاندن ویژگی‌های خالی در فهرست:

`systemctl show {{[-a|--all]}}`

- نمایش فقط ویژگی‌های مشخص:

`systemctl show {{unit}} {{[-p|--property]}} {{Wants,Conflicts,...}}`
