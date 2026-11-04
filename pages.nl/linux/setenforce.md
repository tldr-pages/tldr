# setenforce

> Schakel SELinux tussen de afdwingende en permissieve modus.
> Om SELinux in of uit te schakelen, bewerk je in plaats daarvan `/etc/selinux/config`.
> Zie ook: `getenforce`, `semanage permissive`.
> Meer informatie: <https://manned.org/setenforce>.

- Zet SELinux in de afdwingende modus:

`setenforce {{1|Enforcing}}`

- Zet SELinux in de permissieve modus:

`setenforce {{0|Permissive}}`
