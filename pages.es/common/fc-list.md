# fc-list

> Lista las fuentes disponibles instaladas en el sistema.
> Más información: <https://manned.org/fc-list>.

- Devuelve una lista de las fuentes instaladas en su sistema:

`fc-list`

- Devuelve una lista de las fuentes instaladas con el nombre dado:

`fc-list | grep '{{DejaVu Serif}}'`

- Devuelve el número de fuentes instaladas con el nombre dado:

`fc-list | wc -l`

- Devuelve una lista de las fuentes instaladas que soportan el idioma basado en su código de idioma:

`fc-list :lang={{jp}}`

- Devuelve una lista de las fuentes instaladas que contienen el glifo especificado por su código Unicode:

`fc-list :charset={{f303}}`
