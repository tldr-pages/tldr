# ya

> Gestiona los paquetes y complementos de Yazi.
> Más información: <https://yazi-rs.github.io/docs/cli>.

- Añade un paquete:

`ya pack -a {{paquete}}`

- Actualiza todos los paquetes:

`ya pack -u`

- Suscribirse a los mensajes de todas las instancias remotas:

`ya sub {{tipos}}`

- Publica un mensaje en la instancia actual con cuerpo de cadena:

`ya pub --str {{cadena_mensaje}}`

- Publica un mensaje a la instancia actual con formato JSON:

`ya pub --json {{mensaje_json}}`

- Publica un mensaje en la instancia especificada con una cadena de texto:

`ya pub-to --str {{mensaje}} {{receptor}} {{tipo}}`
