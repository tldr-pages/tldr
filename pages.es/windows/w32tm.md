# w32tm

> Consulta y controla el servicio de sincronización de tiempo w32time.
> Más información: <https://learn.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings>.

- Muestra el estado actual de la sincronización de tiempo:

`w32tm /query /status /verbose`

- Muestra un gráfico de desfase de tiempo contra un servidor horario:

`w32tm /stripchart /computer:{{servidor_de_tiempo}}`

- Muestra una respuesta NTP de un servidor horario:

`w32tm /stripchart /packetinfo /samples:1 /computer:{{servidor_de_tiempo}}`

- Muestra el estado de los servidores de tiempo usados actualmente:

`w32tm /query /peers`

- Muestra la configuración del servicio w32time (ejecutar en consola con privilegios elevados):

`w32tm /query /configuration`

- Fuerza la resincronización de tiempo inmediatamente (ejecutar en consola con privilegios elevados):

`w32tm /resync /force`

- Escribe los registros de depuración de w32time en un archivo (ejecutar en consola con privilegios elevados):

`w32tm /debug /enable /file:{{ruta\a\debug.log}} /size:{{10000000}} /entries:{{0-300}}`
