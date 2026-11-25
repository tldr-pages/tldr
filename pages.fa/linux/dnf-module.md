# dnf module

> مدیریت ماژولار بودن بسته‌ها.
> اطلاعات بیشتر: <https://dnf.readthedocs.io/en/latest/command_ref.html#module-command>.

- مشاهدهٔ نمای کلی ماژول‌ها:

`dnf module list`

- مشاهدهٔ ماژول‌های یک برنامهٔ مشخص:

`dnf module list {{package_name}}`

- فعال کردن یک بسته:

`sudo dnf module enable {{package_name}}:{{stream}}`

- فعال کردن و نصب یک نسخهٔ مشخص:

`dnf module install {{package_name}}:{{stream}}`
