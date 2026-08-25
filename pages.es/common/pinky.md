# pinky

> Imprime información del usuario mediante el protocolo `finger`.
> Más información: <https://manned.org/pinky>.

- Muestra detalles sobre el usuario actual:

`pinky`

- Muestra detalles de un usuario específico:

`pinky {{usuario}}`

- Muestra detalles en formato extenso:

`pinky {{usuario}} -l`

- Omite el directorio de inicio y el intérprete de comandos del usuario en formato largo:

`pinky {{usuario}} -lb`

- Omite el archivo de proyecto del usuario en formato largo:

`pinky {{usuario}} -lh`

- Omite los encabezados de columna en formato corto:

`pinky {{usuario}} -f`
