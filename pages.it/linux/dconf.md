# dconf

> Gestisce i database dconf.
> Vedi anche: `dconf read`, `dconf reset`, `dconf write`, `gsettings`.
> Maggiori informazioni: <https://manned.org/dconf>.

- Stampa il valore di una chiave specifica:

`dconf read /{{path/to/key}}`

- Stampa le sottodirectory e le sotto-chiavi di un percorso specifico:

`dconf list /{{percorso/della/directory}}/`

- Scrive il valore di una chiave specifica:

`dconf write /{{path/to/key}} "{{valore}}"`

- Reimposta il valore di una chiave specifica:

`dconf reset /{{path/to/key}}`

- Osserva una chiave/directory specifica per rilevare modifiche:

`dconf watch /{{path/to/key|/path/to/directory}}/`

- Mostra una directory specifica in formato file INI:

`dconf dump /{{percorso/della/directory}}/`
