# fail2ban-client

> پیکربندی و کنترل سرور fail2ban.
> اطلاعات بیشتر: <https://manned.org/fail2ban-client>.

- نمایش وضعیت کلی سرور fail2ban و فهرست jailهای فعال:

`fail2ban-client status`

- نمایش وضعیت یک jail مشخص:

`fail2ban-client status {{jail}}`

- حذف یک IP مشخص از فهرست مسدودسازی یک jail:

`fail2ban-client set {{jail}} unbanip {{ip_address}}`

- بررسی در حال اجرا بودن سرور fail2ban:

`fail2ban-client ping`
