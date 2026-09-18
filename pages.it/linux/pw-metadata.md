# pw-metadata

> Monitora, imposta ed elimina metadati sugli oggetti PipeWire.
> Vedi anche: `pipewire`, `pw-mon`, `pw-cli`.
> Maggiori informazioni: <https://docs.pipewire.org/page_man_pw-metadata_1.html>.

- Mostra i metadati nel nome `default`:

`pw-metadata`

- Mostra i metadati con ID 0 in `settings`:

`pw-metadata {{[-n|--name]}} {{settings}} {{0}}`

- Elenca tutti gli oggetti metadati disponibili:

`pw-metadata {{[-l|--list]}}`

- Rimane in esecuzione e registra le modifiche ai metadati:

`pw-metadata {{[-m|--monitor]}}`

- Elimina tutti i metadati:

`pw-metadata {{[-d|--delete]}}`

- Imposta `log.level` a 1 in `settings`:

`pw-metadata {{[-n|--name]}} {{settings}} {{0}} {{log.level}} {{1}}`

- Mostra aiuto:

`pw-metadata {{[-h|--help]}}`
