# ip route list

> زیردستور نمایش برای مدیریت جدول مسیریابی IP.
> اطلاعات بیشتر: <https://manned.org/ip-route>.

- نمایش جدول مسیریابی `main`:

`ip {{[r|route]}} {{[l|list]}}`

- نمایش جدول مسیریابی اصلی (همان مثال نخست):

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{main|254}}`

- نمایش جدول مسیریابی محلی:

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{local|255}}`

- نمایش همهٔ جدول‌های مسیریابی:

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{all|unspec|0}}`

- فهرست کردن فقط مسیرهای یک دستگاه مشخص:

`ip {{[r|route]}} {{[l|list]}} dev {{ethX}}`

- فهرست کردن مسیرهای محدودهٔ مشخص:

`ip {{[r|route]}} {{[l|list]}} {{[s|scope]}} link`

- نمایش حافظهٔ نهان مسیریابی:

`ip {{[r|route]}} {{[l|list]}} {{[c|cache]}}`

- نمایش فقط مسیرهای IPv6 یا IPv4:

`ip {{-6|-4}} {{[r|route]}}`
