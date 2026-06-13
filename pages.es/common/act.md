# act

> Ejecuta GitHub Actions localmente usando Docker.
> Más información: <https://manned.org/act>.

- Lista los trabajos disponibles:

`act {{[-l|--list]}}`

- Ejecuta el evento por defecto:

`act`

- Ejecuta un evento específico:

`act {{event_type}}`

- Ejecuta un trabajo específico:

`act {{[-j|--job]}} {{job_id}}`

- No ejecuta realmente las acciones (es decir, una ejecución en seco):

`act {{[-n|--dryrun]}}`

- Muestra registros detallados:

`act {{[-v|--verbose]}}`

- Ejecuta un flujo de trabajo específico con el evento push:

`act push {{[-W|--workflows]}} {{ruta/al/flujo_de_trabajo}}`
