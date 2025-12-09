# for

> Ejecutar condicionalmente un comando varias veces.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/for>.

- Ejecutar los comandos dados para el conjunto especificado:

`for %{{variable}} in ({{elemento_a elemento_b elemento_c}}) do ({{echo Se ejecuta el bucle}})`

- Iterar sobre un rango dado de números:

`for /l %{{variable}} in ({{desde}}, {{paso}}, {{hasta}}) do ({{echo Se ejecuta el bucle}})`

- Iterar sobre una lista dada de archivos:

`for %{{variable}} in ({{ruta\al\archivo1.ext ruta\al\archivo2.ext ...}}) do ({{echo Se ejecuta el bucle}})`

- Iterar sobre una lista dada de directorios:

`for /d %{{variable}} in ({{ruta\al\directorio1.ext ruta\al\directorio2.ext ...}}) do ({{echo Se ejecuta el bucle}})`

- Realizar un comando dado en cada directorio:

`for /d %{{variable}} in (*) do (if exist %{{variable}} {{echo Se ejecuta el bucle}})`
