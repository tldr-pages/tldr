# pw-cli

> Beheer de modules, objecten, nodes, apparaten, links en nog veel meer van een PipeWire-instantie.
> Zie ook: `wpctl`.
> Meer informatie: <https://docs.pipewire.org/page_man_pw-cli_1.html>.

- Toon informatie van alle objecten van een specifiek type:

`pw-cli {{[ls|list-objects]}} {{Node|Link|Port|Client|Device|Metadata|Factory|Module|Profiler|SecurityContext|Core}}`

- Toon informatie over een object met een specifieke ID:

`pw-cli {{[i|info]}} {{4}}`

- Toon informatie van alle objecten:

`pw-cli {{[i|info]}} all`

- Monitor objectwijzigingen:

`pw-cli {{[-m|--monitor]}}`

- Toon de help:

`pw-cli {{[h|help]}}`
