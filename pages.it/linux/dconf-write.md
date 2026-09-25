# dconf write

> Scrive i valori delle chiavi nei database dconf.
> Vedi anche: `dconf`.
> Maggiori informazioni: <https://manned.org/dconf>.

- Scrive il valore di una chiave specifica:

`dconf write /{{path/to/key}} "{{value}}"`

- Scrive il valore di una chiave stringa specifica:

`dconf write /{{path/to/key}} "'{{string}}'"`

- Scrive il valore di una chiave intera specifica:

`dconf write /{{path/to/key}} "{{5}}"`

- Scrive il valore di una chiave booleana specifica:

`dconf write /{{path/to/key}} "{{true|false}}"`

- Scrive il valore di una chiave array specifica:

`dconf write /{{path/to/key}} "[{{'first', 'second', ...}}]"`

- Scrive il valore di una chiave array vuota specifica:

`dconf write /{{path/to/key}} "@as []"`
