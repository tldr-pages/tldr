# adb logcat

> Vuelca un registro de mensajes del sistema.
> Más información: <https://developer.android.com/tools/logcat>.

- Muestra registros del sistema:

`adb logcat`

- Muestra las líneas que coincidan con una expresión regular:

`adb logcat -e {{expresión_regular}}`

- Muestra los registros de una etiqueta en un modo específico ([V]erboso, [D]epuración, [I]nformación, [W]arning, [E]rror, [F]atal, [S]ilencioso), filtrando otras etiquetas:

`adb logcat {{etiqueta}}:{{modo}} *:S`

- Muestra los registros de aplicaciones React Native en modo [V]erboso [S]ilenciando otras etiquetas:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Muestra los registros de todas las etiquetas con nivel de prioridad [W]arning y superior:

`adb logcat *:W`

- Muestra los registros de un proceso específico:

`adb logcat --pid {{pid}}`

- Muestra los registros del proceso de un paquete específico:

`adb logcat --pid $(adb shell pidof -s {{paquete}})`

- Colorea el registro (normalmente se usan filtros):

`adb logcat -v color`
