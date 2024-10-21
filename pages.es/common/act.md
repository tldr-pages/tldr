# act

> Ejecuta acciones de GitHub localmente mediante Docker.
> Más información: <https://github.com/nektos/act>.

- Lista las acciones disponibles:

`act -l`

- Ejecuta el evento por defecto:

`act`

- Ejecuta un evento específico:

`act {{tipo_de_evento}}`

- Ejecuta una acción específica:

`act -j {{identificador_de_acción}}`

- Simula una acción:

`act -n`

- Muestra registros detallados:

`act -v`

- Ejecuta un flujo de trabajo específico con el evento push:

`act push -W {{ruta/a/flujo_de_trabajo}}`
