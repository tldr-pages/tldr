# driverquery

> Mostra información sobre los controladores de dispositivo instalados.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/driverquery>.

- Mostra una lista de todos los controladores de dispositivo instalados:

`driverquery`

- Mostra una lista de controladores en el formato especificado:

`driverquery /fo {{tabla|lista|csv}}`

- Mostra una lista de controladores con una columna que indique si están firmados:

`driverquery /si`

- Excluir el encabezado en la lista de salida:

`driverquery /nh`

- Mostra una lista de controladores para una máquina remota:

`driverquery /s {{nombre_del_host}} /u {{nombre_de_usuario}} /p {{contraseña}}`

- Mostra una lista de controladores con información detallada:

`driverquery /v`

- Mostra ayuda:

`driverquery /?`
