# nmcli radio

> نمایش وضعیت سوئیچ‌های رادیویی یا فعال و غیرفعال کردن آن‌ها با NetworkManager.
> اطلاعات بیشتر: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#radio>.

- نمایش وضعیت Wi-Fi:

`nmcli {{[r|radio]}} {{[w|wifi]}}`

- روشن یا خاموش کردن Wi-Fi:

`nmcli {{[r|radio]}} {{[w|wifi]}} {{on|off}}`

- نمایش وضعیت WWAN:

`nmcli {{[r|radio]}} {{[ww|wwan]}}`

- روشن یا خاموش کردن WWAN:

`nmcli {{[r|radio]}} {{[ww|wwan]}} {{on|off}}`

- نمایش وضعیت هر دو سوئیچ:

`nmcli {{[r|radio]}}`

- روشن یا خاموش کردن هر دو سوئیچ:

`nmcli {{[r|radio]}} {{[a|all]}} {{on|off}}`
