# setenforce

> Toggle SELinux between enforcing and permissive modes.
> To enable or disable SELinux, edit `/etc/selinux/config` instead.
> See also: `getenforce`, `semanage-permissive`.
> More information: <https://manned.org/man/setenforce>.

- Put SELinux in enforcing mode:

`setenforce {{1|Enforcing}}`

- Put SELiunx in permissive mode:

`setenforce {{0|Permissive}}`
