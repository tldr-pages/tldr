# semanage permissive

> Gestiona dominios SELinux en modo permisivo de forma persistente.
> Ten en cuenta que esto, en la práctica, hace que el proceso quede sin restricciones. Para un uso a largo plazo, se recomienda configurar SELinux correctamente.
> Vea también: `semanage`, `getenforce`, `setenforce`.
> Más información: <https://manned.org/semanage-permissive>.

- Muestra todos los tipos de proceso (también conocidos como dominios) que se encuentran en modo permisivo:

`sudo semanage permissive {{[-l|--list]}}`

- Establece el modo permisivo para un dominio:

`sudo semanage permissive {{[-a|--add]}} {{httpd_t}}`

- Desactiva el modo permisivo para un dominio:

`sudo semanage permissive {{[-d|--delete]}} {{httpd_t}}`
