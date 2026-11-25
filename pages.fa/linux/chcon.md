# chcon

> تغییر زمینهٔ امنیتی SELinux برای یک یا چند فایل یا دایرکتوری.
> همچنین ببینید: `secon`, `restorecon`, `semanage fcontext`.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/chcon-invocation.html>.

- مشاهدهٔ زمینهٔ امنیتی یک فایل:

`ls {{[-lZ|-l --context]}} {{path/to/file}}`

- تغییر زمینهٔ امنیتی فایل هدف با استفاده از یک فایل مرجع:

`chcon --reference {{reference_file}} {{target_file}}`

- تغییر کامل زمینهٔ امنیتی SELinux یک فایل:

`chcon {{user}}:{{role}}:{{type}}:{{range/level}} {{filename}}`

- تغییر فقط بخش کاربر زمینهٔ امنیتی SELinux:

`chcon {{[-u|--user]}} {{user}} {{filename}}`

- تغییر فقط بخش نقش زمینهٔ امنیتی SELinux:

`chcon {{[-r|--role]}} {{role}} {{filename}}`

- تغییر فقط بخش نوع زمینهٔ امنیتی SELinux:

`chcon {{[-t|--type]}} {{type}} {{filename}}`

- تغییر فقط بخش بازه یا سطح زمینهٔ امنیتی SELinux:

`chcon {{[-l|--range]}} {{range/level}} {{filename}}`
