# dirb

> پویش وب‌سرورهای مبتنی بر HTTP برای یافتن دایرکتوری‌ها و فایل‌ها.
> اطلاعات بیشتر: <https://manned.org/dirb>.

- پویش یک وب‌سرور با فهرست واژه‌های پیش‌فرض:

`dirb {{https://example.org}}`

- پویش یک وب‌سرور با فهرست واژه‌های دلخواه:

`dirb {{https://example.org}} {{path/to/wordlist.txt}}`

- پویش غیربازگشتی یک وب‌سرور:

`dirb {{https://example.org}} -r`

- پویش یک وب‌سرور با عامل کاربر و کوکی مشخص برای درخواست‌های HTTP:

`dirb {{https://example.org}} -a {{user_agent_string}} -c {{cookie_string}}`
