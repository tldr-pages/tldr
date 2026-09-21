# driverquery

> Muestra información sobre los controladores de dispositivo instalados.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/driverquery>.

- Muestra una lista de todos los controladores de dispositivo instalados:

`driverquery`

- Muestra una lista de controladores en el formato especificado:

`driverquery /fo {{tabla|lista|csv}}`

- Muestra una lista de controladores con una columna que indique si están firmados:

`driverquery /si`

- Excluye el encabezado en la lista de salida:

`driverquery /nh`

- Muestra una lista de controladores para una máquina remota:

`driverquery /s {{nombre_del_host}} /u {{nombre_de_usuario}} /p {{contraseña}}`

- Muestra una lista de controladores con información detallada:

`driverquery /v`

- Mostra ayuda:

`driverquery /?`
