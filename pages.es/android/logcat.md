# logcat

> Vuelca un registro de mensajes del sistema, incluyendo seguimientos de pila cuando ocurren errores, y mensajes informativos enviados por las aplicaciones.
> Más información: <https://developer.android.com/tools/logcat>.

- Muestra registros del sistema:

`logcat`

- Escribe registros del sistema a un archivo:

`logcat -f {{ruta/al/archivo}}`

- Muestra registros que coincidan con una expresión regular:

`logcat --regex {{expresión_regular}}`

- Muestra registros de un proceso específico:

`logcat --pid {{pid}}`

- Muestra registros del proceso de un paquete específico:

`logcat --pid $(pidof -s {{paquete}})`
