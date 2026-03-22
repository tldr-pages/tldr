# lsb_release

> Proporciona información específica de la distribución y LSB (Linux Standard Base).
> Más información: <https://manned.org/lsb_release>.

- Muestra toda la información disponible:

`lsb_release {{[-a|--all]}}`

- Muestra una descripción del sistema operativo (normalmente el nombre completo):

`lsb_release {{[-d|--description]}}`

- Muestra solo el nombre del sistema operativo (ID) sin el campo nombre:

`lsb_release {{[-is|--id --short]}}`

- Muestra el número de versión y el nombre en clave de la distribución sin el campo de nombre:

`lsb_release {{[-rcs|--release --codename --short]}}`
