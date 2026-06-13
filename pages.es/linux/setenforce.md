# setenforce

> Alterna SELinux entre los modos de aplicación y permisivo.
> Para habilitar o deshabilitar SELinux, edita `/etc/selinux/config`.
> Vea también: `getenforce`, `semanage-permissive`.
> Más información: <https://manned.org/setenforce>.

- Activa el modo de aplicación de SELinux:

`setenforce {{1|Enforcing}}`

- Activa el modo permisivo de SELinux:

`setenforce {{0|Permissive}}`
