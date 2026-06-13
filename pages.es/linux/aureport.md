# aureport

> Genera informes resumidos de los registros de auditd.
> Más información: <https://manned.org/aureport>.

- Muestra un resumen de los eventos de auditd:

`sudo aureport`

- Genera un resumen de los eventos de inicio de sesión:

`sudo aureport {{[-l|--login]}}`

- Muestra todos los informes de llamadas al sistema:

`sudo aureport {{[-s|--syscall]}}`

- Genera un resumen de eventos ejecutables:

`sudo aureport {{[-x|--executable]}}`

- Muestra un resumen de eventos para un intervalo de tiempo específico:

`sudo aureport {{[-ts|--start]}} {{tiempo_inicial}} {{[-te|--end]}} {{tiempo_final}}`

- Muestra todos los archivos de auditoría y el intervalo de tiempo de los eventos que cubren:

`sudo aureport {{[-t|--log-time]}}`

- Muestra la ayuda:

`aureport --help`
