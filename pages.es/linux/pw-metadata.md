# pw-metadata

> Supervisa, establece y elimina metadatos en objetos PipeWire.
> Vea también: `pipewire`, `pw-mon`, `pw-cli`.
> Más información: <https://docs.pipewire.org/page_man_pw-metadata_1.html>.

- Muestra metadatos en formato `predeterminado`:

`pw-metadata`

- Muestra metadatos con ID 0 en `configuración`:

`pw-metadata {{-n|--name}} {{settings}} {{0}}`

- Lista todos los objetos de metadatos disponibles:

`pw-metadata {{-l|--list}}`

- Sigue ejecutando y registrando los cambios en los metadatos:

`pw-metadata {{-m|--monitor}}`

- Elimina todos los metadatos:

`pw-metadata {{-d|--delete}}`

- Ajusta `log.level` a 1 en `configuración`:

`pw-metadata --name {{settings}} {{0}} {{log.level}} {{1}}`

- Muestra ayuda:

`pw-metadata --help`
