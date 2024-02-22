# adb logcat

> Vuelca un registro de mensajes del sistema.
> Más información: <https://developer.android.com/tools/logcat>.

- Muestra registros del sistema:

`adb logcat`

- Muestra las líneas que coinciden con una expresión regular:

`adb logcat -e {{expresion_regular}}`

- Muestra los registros de una etiqueta en un modo específico ([V]erbose, [D]ebug, [I]nfo, [W]arning, [E]rror, [F]atal, [S]ilent), filtrando otras etiquetas:

`adb logcat {{etiqueta}}:{{modo}} *:S`

- Muestra los registros de aplicaciones React Native en modo [V]erbose [S]ilencing otras etiquetas:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Muestra los registros de todas las etiquetas con nivel de prioridad [W]arning y superior:

`adb logcat *:W`

- Muestra los registros de un proceso específico:

`adb logcat --pid={{pid}}`

- Muestra los registros del proceso de un paquete específico:

`adb logcat --pid=$(adb shell pidof -s {{paquete}})`

- Colorea el registro (normalmente se utiliza con filtros):

`adb logcat -v color`
