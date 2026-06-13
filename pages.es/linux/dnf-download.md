# dnf download

> Descarga paquetes RPM desde los repositorios DNF.
> No predeterminado en `dnf` pero admitido a través de `dnf-plugins-core`.
> Vea también: `dnf`.
> Más información: <https://dnf-plugins-core.readthedocs.io/en/latest/download.html>.

- Descarga la última versión de un paquete al directorio actual:

`dnf download {{paquete}}`

- Descarga un paquete a un directorio específico (el directorio debe existir):

`dnf download {{paquete}} --destdir {{ruta/al/directorio}}`

- Imprime la URL desde la que se puede descargar el paquete RPM:

`dnf download --url {{paquete}}`
