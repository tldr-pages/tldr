# adb connect

> Permite establecer una conexión a un dispositivo Android de forma inalámbrica.
> Más información: <https://developer.android.com/tools/adb>.

- Empareja con un dispositivo Android (los códigos de dirección y emparejamiento se pueden encontrar en las opciones de desarrollador):

`adb pair {{dirección_ip}}:{{puerto}}`

- Conecta con un dispositvo Android (el puerto será diferente del de emparejamiento):

`adb connect {{dirección_ip}}:{{puerto}}`

- Desconecta un dispositivo:

`adb disconnect {{dirección_ip}}:{{puerto}}`
