# iostat

> Informa las estadísticas de los dispositivos.
> Más información: <https://ss64.com/mac/iostat.html>.

- Muestra estadísticas instantáneas de dispositivos (KB/t, transferencias y MB por segundo), estadísticas de CPU (porcentajes de tiempo empleado en modos usuario, sistema e inactivo) y promedios de carga del sistema (para los últimos 1, 5 y 15 min):

`iostat`

- Muestra solo estadísticas de dispositivos:

`iostat -d`

- Muestra informes incrementales de estadísticas de CPU y disco cada 2 segundos:

`iostat 2`

- Muestra las estadísticas del primer disco cada segundo de forma indefinida:

`iostat -w 1 disk0`

- Muestra las estadísticas del segundo disco cada 3 segundos, 10 veces:

`iostat -w 3 -c 10 disk1`

- Muestra utilizando la antigua muestra de `iostat`. Muestra los sectores transferidos por segundo, las transferencias por segundo, el promedio de milisegundos por transacción y las estadísticas de la CPU + los promedios de carga de la muestra por defecto:

`iostat -o`

- Muestra las estadísticas totales del dispositivo (KB/t: kilobytes por transferencia como antes, xfrs: número total de transferencias, MB: número total de megabytes transferidos):

`iostat -I`
