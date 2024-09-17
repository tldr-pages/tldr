# automount

> Lee el archivo `/etc/auto_master` y monta `autofs` en los puntos de montaje apropiados para activar el montaje bajo demanda de directorios. Esencialmente, es una forma de iniciar manualmente el proceso de automontaje del sistema.
> Nota: Lo más probable es que necesites ejecutarlo con `sudo` si no tienes los permisos necesarios.
> Más información: <https://keith.github.io/xcode-man-pages/automount.8.html>.

- Ejecuta automount, vacía la caché(`-c`) de antemano, y es detallista(`-v`) al respecto (uso más común):

`automount -cv`

- Desmonta automáticamente transcurridos 5 minutos (300 segundos) de inactividad:

`automount -t 300`

- Desmonta cualquier cosa previamente montada por automount y/o definida en `/etc/auto_master`:

`automount -u`
