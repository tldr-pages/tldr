# runcon

> اجرای برنامه در زمینهٔ امنیتی SELinux متفاوت.
> همچنین ببینید: `secon`.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/runcon-invocation.html>.

- چاپ زمینهٔ امنیتی زمینهٔ اجرای فعلی:

`runcon`

- تعیین دامنه برای اجرای دستور در آن:

`runcon {{[-t|--type]}} {{domain}}_t {{command}}`

- تعیین نقش زمینه برای اجرای دستور با آن:

`runcon {{[-r|--role]}} {{role}}_r {{command}}`

- تعیین زمینهٔ کامل برای اجرای دستور با آن:

`runcon {{user}}_u:{{role}}_r:{{domain}}_t {{command}}`
