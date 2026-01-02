# farge

> Muestra el color de un píxel específico de la pantalla en formatos hexadecimal o RGB.
> Más información: <https://github.com/sdushantha/farge#usage>.

- Muestra una pequeña ventana de vista previa del color de un píxel con su valor hexadecimal, y copia este valor al portapapeles:

`farge`

- Copia el valor hexadecimal de un píxel al portapapeles sin mostrar una ventana de vista previa:

`farge --no-preview`

- Envía el valor hexadecimal de un píxel a `stdout` y copia este valor al portapapeles:

`farge --stdout`

- Envía el valor RGB de un píxel a `stdout` y copia este valor al portapapeles:

`farge --rgb --stdout`

- Muestra el valor hexadecimal de un píxel como notificación que expira en 5000 milisegundos y copia este valor al portapapeles:

`farge --notify --expire-time 5000`
