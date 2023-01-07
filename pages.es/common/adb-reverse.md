# adb reverse

> Android Debug Bridge Reverse: conexiones de socket inversas desde una instancia de emulador de Android o dispositivos Android conectados.
> Más información: <https://developer.android.com/studio/command-line/adb>.

- Lista de todas las conexiones de socket inverso de emuladores y dispositivos:

`adb reverse --list`

- Invertir un puerto TCP desde un emulador o dispositivo a localhost:

`adb reverse tcp:{{remote_port}} tcp:{{local_port}}`

- Eliminar una conexión de socket inversa de un emulador o dispositivo:

`adb reverse --remove tcp:{{remote_port}}`

- Elimina todas las conexiones de socket inverso de todos los emuladores y dispositivos:

`adb reverse --remove-all`
