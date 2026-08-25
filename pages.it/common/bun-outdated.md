# bun outdated

> Elenca le dipendenze per le quali sono disponibili versioni più recenti.
> Maggiori informazioni: <https://bun.com/docs/pm/cli/outdated>.

- Elenca tutte le dipendenze obsolete nel progetto corrente:

`bun outdated`

- Controlla se un pacchetto specifico è obsoleto:

`bun outdated {{package}}`

- Elenca le dipendenze obsolete corrispondenti a un pattern glob:

`bun outdated "{{pattern}}"`

- Mostra le dipendenze obsolete per workspace specifici:

`bun outdated {{[-F|--filter]}} "{{workspace_pattern}}"`

- Controlla ricorsivamente tutti i workspace in un monorepo:

`bun outdated {{[-r|--recursive]}}`
