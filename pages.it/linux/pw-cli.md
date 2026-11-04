# pw-cli

> Gestisce moduli, oggetti, nodi, dispositivi, collegamenti e molto altro di un'istanza PipeWire.
> Vedi anche: `wpctl`.
> Maggiori informazioni: <https://docs.pipewire.org/page_man_pw-cli_1.html>.

- Stampa informazioni di tutti gli oggetti di un tipo specifico:

`pw-cli {{[ls|list-objects]}} {{Node|Link|Port|Client|Device|Metadata|Factory|Module|Profiler|SecurityContext|Core}}`

- Stampa informazioni su un oggetto con un ID specifico:

`pw-cli {{[i|info]}} {{4}}`

- Stampa le informazioni di tutti gli oggetti:

`pw-cli {{[i|info]}} all`

- Monitora le modifiche agli oggetti:

`pw-cli {{[-m|--monitor]}}`

- Mostra aiuto:

`pw-cli {{[h|help]}}`
