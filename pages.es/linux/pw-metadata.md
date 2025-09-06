# pw-metadata

> Supervisa, establece y elimina metadatos en objetos PipeWire.
> Vea también: `pipewire`, `pw-mon`, `pw-cli`.
> Más información: <https://docs.pipewire.org/page_man_pw-metadata_1.html>.

- Muestra metadatos en el formato por defecto:

`pw-metadata`

- Muestra metadatos con el identificador 0 en `settings`:

`pw-metadata {{[-n|--name]}} {{settings}} {{0}}`

- Lista todos los objetos de metadatos disponibles:

`pw-metadata {{[-l|--list]}}`

- Continua ejecutando y registrando los cambios en los metadatos:

`pw-metadata {{[-m|--monitor]}}`

- Elimina todos los metadatos:

`pw-metadata {{[-d|--delete]}}`

- Ajusta `log.level` a 1 en `settings`:

`pw-metadata {{[-n|--name]}} {{settings}} {{0}} {{log.level}} {{1}}`

- Muestra ayuda:

`pw-metadata {{[-h|--help]}}`
