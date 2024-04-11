# last

> Lista la información de los últimos inicios de sesión de usuario.
> Vea también: `lastb`, `login`.
> Más información: <https://manned.org/last.1>.

- Lista la información de inicio de sesión (por ejemplo, nombre de usuario, terminal, tiempo de arranque, núcleo) de todos los usuarios:

`last`

- Lista la información de inicio de sesión de un usuario específico:

`last {{nombre_de_usuario}}`

- Muestra la información de una terminal específica:

`last {{tty1}}`

- Lista la información actualizada (por defecto, la más reciente aparece al principio):

`last | tac`

- Muestra información sobre el arranque del sistema:

`last "{{system boot}}"`

- Lista información con un formato de [t]iempo específico:

`last --time-format {{notime|full|iso}}`

- Lista información desde una fecha y hora específica:

`last --since {{-7days}}`

- Muestra información (es decir, nombre e IP) de hosts remotos:

`last --dns`
