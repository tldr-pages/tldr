# dd

> Convierte y copia un archivo.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html>.

- Crea una unidad USB de arranque a partir de un archivo isohybrid (como `archlinux-xxx.iso`) y muestra el progreso:

`dd if={{ruta/al/archivo.iso}} of={{/dev/unidad_usb}} status=progress`

- Clona una unidad a otra con un tamaño de bloque de 4 MiB y descarga las escrituras antes de que el comando termine:

`dd bs=4M conv=fsync if={{/dev/unidad_de_origen}} of={{/dev/unidad_de_descarga}}`

- Genera un archivo con un número específico de bytes aleatorios utilizando el controlador aleatorio del kernel:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{ruta/al/archivo_aleatorio}}`

- Compara el rendimiento de escritura de un disco:

`dd bs={{1M}} count={{1024}} if=/dev/zero of={{ruta/al/fichero_1GB}}`

- Crea una copia de seguridad del sistema en un archivo IMG (puede restaurarla más tarde intercambiando `if` y `of`), y muestra el progreso:

`dd if={{/dev/unidad_dispositivo}} of={{ruta/al/archivo.img}} status=progress`

- Comprueba el progreso de una operación `dd` en curso (ejecute este comando desde otro intérprete de comandos):

`kill -USR1 $(pgrep -x dd)`
