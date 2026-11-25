# nmcli networking

> مدیریت وضعیت شبکهٔ NetworkManager.
> اطلاعات بیشتر: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#networking>.

- نمایش وضعیت شبکهٔ NetworkManager:

`nmcli {{[n|networking]}}`

- فعال یا غیرفعال کردن شبکه و همهٔ واسط‌های مدیریت‌شده توسط NetworkManager:

`nmcli {{[n|networking]}} {{on|off}}`

- نمایش آخرین وضعیت شناخته‌شدهٔ اتصال:

`nmcli {{[n|networking]}} {{[c|connectivity]}}`

- نمایش وضعیت فعلی اتصال:

`nmcli {{[n|networking]}} {{[c|connectivity]}} {{[c|check]}}`
