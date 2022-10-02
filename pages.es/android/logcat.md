# logcat

> Vuelca un registro de mensajes del sistema, incluidos los seguimientos de pila, los casos de error del sistema y los mensajes que escribes desde tu app con la clase Log.
> Más información: <https://developer.android.com/studio/command-line/logcat>.

- Mostrar registros del sistema:

`logcat`

- Escribir registros del sistema a un archivo:

`logcat -f {{ruta/al/archivo}}`

- Mostrar líneas que coincidan con una expresión regular:

`logcat --regex {{expresión_regular}}`
