# if

> Realiza procesamiento condicional en scripts por lotes.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/if>.

- Ejecuta los comandos especificados si la condición es verdadera:

`if {{condición}} ({{echo La condición es verdadera}})`

- Ejecuta los comandos especificados si la condición es falsa:

`if not {{condición}} ({{echo La condición es verdadera}})`

- Ejecuta los primeros comandos especificados si la condición es verdadera, de lo contrario, ejecuta los segundos comandos especificados:

`if {{condición}} ({{echo La condición es verdadera}}) else ({{echo La condición es falsa}})`

- Verifica si `%errorlevel%` es mayor o igual al código de salida especificado:

`if errorlevel {{2}} ({{echo La condición es verdadera}})`

- Verifica si dos cadenas son iguales:

`if %{{variable}}% == {{cadena}} ({{echo La condición es verdadera}})`

- Verifica si dos cadenas son iguales sin respetar el caso de las letras:

`if /i %{{variable}}% == {{cadena}} ({{echo La condición es verdadera}})`

- Verifica si un archivo existe:

`if exist {{ruta\al\archivo}} ({{echo La condición es verdadera}})`
