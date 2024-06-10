# dd

> Convierte y copia un archivo.
> Más información: <https://keith.github.io/xcode-man-pages/dd.1.html>.

- Crea una unidad USB de arranque desde un archivo isohybrid (como `archlinux-xxx.iso`) y muestra el progreso:

`dd if={{ruta/al/archivo.iso}} of={{/dev/dispositivo_usb}} status=progress`

- Clona una unidad a otra unidad con un bloque de 4 MB, ignora el error y muestra el progreso:

`dd bs=4m conv=noerror if={{/dev/dispositivo_de origen}} of={{/dev/dispositivo_de destino}} status=progress`

- Genera un archivo con un número específico de bytes aleatorios utilizando el controlador aleatorio del núcleo:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{ruta/al/archivo_aleatorio}}`

- Compara el rendimiento de escritura de un disco:

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{ruta/para/archivo_1GB}}`

- Genera una copia de seguridad del sistema en un archivo IMG y muestra el progreso:

`dd if={{/dev/dispositivo_unidad}} of={{ruta/al/archivo.img}} status=progress`

- Comprueba el progreso de una operación `dd` en curso (ejecuta este comando desde otro intérprete de comandos):

`kill -USR1 $(pgrep ^dd)`
