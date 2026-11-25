# nmcli agent

> اجرای `nmcli` به‌عنوان عامل اطلاعات محرمانهٔ NetworkManager یا عامل polkit.
> اطلاعات بیشتر: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#agent>.

- ثبت `nmcli` به‌عنوان عامل اطلاعات محرمانه و گوش دادن به درخواست‌های آن:

`nmcli {{[a|agent]}} {{[s|secret]}}`

- ثبت `nmcli` به‌عنوان عامل polkit و گوش دادن به درخواست‌های مجوز:

`nmcli {{[a|agent]}} {{[p|polkit]}}`

- ثبت `nmcli` به‌عنوان عامل اطلاعات محرمانه و عامل polkit:

`nmcli {{[a|agent]}} {{[a|all]}}`
