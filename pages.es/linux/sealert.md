# sealert

> Analiza y explica los mensajes de denegación AVC de SELinux.
> Forma parte del paquete `setroubleshoot-server`.
> Vea también: `audit2why`, `ausearch`, `audit2allow`.
> Más información: <https://manned.org/sealert>.

- Analiza todas las denegaciones recientes de SELinux:

`sudo sealert {{[-a|--analyze]}} {{/var/log/audit/audit.log}}`

- Analiza un ID de alerta específico de los registros del sistema:

`sudo sealert {{[-l|--lookupid]}} {{id_alerta}}`

- Muestra un resumen de las alertas recientes de SELinux:

`sudo sealert {{[-b|--browser]}}`

- Supervisa el registro de auditoría en tiempo real en busca de nuevas alertas:

`sudo tail {{[-f|--follow]}} {{/var/log/audit/audit.log}} | sealert {{[-l|--lookupid]}} -`
