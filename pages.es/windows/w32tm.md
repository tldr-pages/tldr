# w32tm

> Consulta y controla el servicio de sincronización de tiempo w32time.
> Más información: <https://learn.microsoft.com/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings>.

- Mostrar el estado actual de la sincronización de tiempo:

`w32tm /query /status /verbose`

- Mostrar un gráfico de desfase de tiempo contra un servidor horario:

`w32tm /stripchart /computer:{{servidor_de_tiempo}}`

- Mostrar una respuesta NTP de un servidor horario:

`w32tm /stripchart /packetinfo /samples:1 /computer:{{servidor_de_tiempo}}`

- Mostrar el estado de los servidores de tiempo usados actualmente:

`w32tm /query /peers`

- Mostrar la configuración del servicio w32time (ejecutar en consola con privilegios elevados):

`w32tm /query /configuration`

- Forzar la resincronización de tiempo inmediatamente (ejecutar en consola con privilegios elevados):

`w32tm /resync /force`

- Escribir los logs de depuración de w32time en un archivo (ejecutar en consola con privilegios elevados):

`w32tm /debug /enable /file:{{ruta\a\debug.log}} /size:{{10000000}} /entries:{{0-300}}`
