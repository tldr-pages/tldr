# prompt

> Cambiar el aviso de estilo DOS predeterminado en una ventana de comandos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/prompt>.

- Restablecer el aviso a la configuración predeterminada:

`prompt`

- Establecer un aviso específico:

`prompt {{aviso}}`

- Cambiar el aviso para mostrar la fecha actual primero:

`prompt $D $P$G`

- Cambiar el aviso para mostrar la hora actual primero:

`prompt $T $P$G`

- Cambiar el aviso añadiendo un texto específico primero:

`prompt {{texto}} $P$G`
