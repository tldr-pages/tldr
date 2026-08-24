# pw-cli

> Gestiona los módulos, objetos, nodos, dispositivos, enlaces y mucho más de una instancia de PipeWire.
> Vea también: `wpctl`.
> Más información: <https://docs.pipewire.org/page_man_pw-cli_1.html>.

- Muestra información sobre todos los objetos de un tipo específico:

`pw-cli {{[ls|list-objects]}} {{Node|Link|Port|Client|Device|Metadata|Factory|Module|Profiler|SecurityContext|Core}}`

- Muestra información sobre un objeto con un ID específico:

`pw-cli {{[i|info]}} {{4}}`

- Muestra la información de todos los objetos:

`pw-cli {{[i|info]}} all`

- Supervisa los cambios en los objetos:

`pw-cli {{[-m|--monitor]}}`

- Muestra la ayuda:

`pw-cli {{[h|help]}}`
