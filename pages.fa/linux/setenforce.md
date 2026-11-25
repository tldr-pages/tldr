# setenforce

> تغییر SELinux بین حالت‌های enforcing و permissive.
> برای فعال یا غیرفعال کردن SELinux به‌جای آن `/etc/selinux/config` را ویرایش کنید.
> همچنین : `getenforce`, `semanage permissive`.
> اطلاعات بیشتر: <https://manned.org/setenforce>.

- قرار دادن SELinux در حالت enforcing:

`setenforce {{1|Enforcing}}`

- قرار دادن SELinux در حالت permissive:

`setenforce {{0|Permissive}}`
