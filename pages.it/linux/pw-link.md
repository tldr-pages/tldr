# pw-link

> Gestisce i collegamenti tra le porte in PipeWire.
> Maggiori informazioni: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- Elenca tutte le porte di output e input audio con i loro ID:

`pw-link {{[-oiI|--output --input --id]}}`

- Crea un collegamento tra una porta di output e una di input:

`pw-link {{nome_porta_output}} {{nome_porta_input}}`

- Scollega due porte:

`pw-link {{[-d|--disconnect]}} {{nome_porta_output}} {{nome_porta_input}}`

- Elenca tutti i collegamenti con i loro ID:

`pw-link {{[-lI|--links --id]}}`

- Mostra aiuto:

`pw-link {{[-h|--help]}}`
