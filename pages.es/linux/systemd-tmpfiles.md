# systemd-tmpfiles

> Crea, elimina y limpia archivos y directorios volátiles y temporales.
> Este comando es invocado automáticamente en el arranque por los servicios systemd, en tanto ejecutarlo manualmente no suele ser necesario.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemd-tmpfiles.html>.

- Crea los archivos y directorios especificados en la configuración:

`systemd-tmpfiles --create`

- Limpia archivos y directorios con los parámetros de edad configurados:

`systemd-tmpfiles --clean`

- Elimina archivos y directorios según lo especificado en la configuración:

`systemd-tmpfiles --remove`

- Aplica operaciones para configuraciones específicas de usuario:

`systemd-tmpfiles --create --user`

- Ejecuta las líneas marcadas para el arranque anticipado:

`systemd-tmpfiles --create --boot`
