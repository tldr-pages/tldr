# adb forward

> Permite conectarse a un dispositivo Android de forma inalámbrica.
> Más información: <https://developer.android.com/tools/adb>.

- Reenvía un puerto TCP:

`adb forward tcp:{{puerto_local}} tcp:{{puerto_remoto}}`

- Enumera todos los reenvíos:

`adb forward --list`

- Elimina una regla de reenvío:

`adb forward --remove tcp:{{puerto_local}}`

- Elimina todas las reglas de reenvío:

`adb forward --remove-all`
