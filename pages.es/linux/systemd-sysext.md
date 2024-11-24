# systemd-sysext

> Activa o desactiva imágenes de extensión del sistema (system extension images).
> Más información: <https://www.freedesktop.org/software/systemd/man/systemd-sysext.html>.

- Lista de imágenes de extensión instaladas:

`systemd-sysext list`

- Combina imágenes de extensión del sistema en `/usr/` y `/opt/`:

`systemd-sysext merge`

- Comprueba el estado de fusión actual:

`systemd-sysext status`

- Separa todas las imágenes de extensión del sistema actualmente instaladas en `/usr/` y `/opt/`:

`systemd-sysext unmerge`

- Actualiza imágenes de extensión del sistema (una combinación de `unmerge` y `merge`):

`systemd-sysext refresh`
