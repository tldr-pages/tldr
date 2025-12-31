# prompt

> Cambia el aviso de estilo DOS predeterminado en una ventana de comandos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/prompt>.

- Restablece el aviso a la configuración predeterminada:

`prompt`

- Establece un aviso específico:

`prompt {{aviso}}`

- Cambia el aviso para mostrar la fecha actual primero:

`prompt $D $P$G`

- Cambia el aviso para mostrar la hora actual primero:

`prompt $T $P$G`

- Cambia el aviso añadiendo un texto específico primero:

`prompt {{texto}} $P$G`
