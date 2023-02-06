# dconf write

> Kulcsértékek írása a dconf adatbázisokba. Lásd még: `dconf`. További információ: <https://manned.org/dconf>.

- Egy adott kulcsérték írása:

`dconf write {{/path/to/key}} "{{value}}"`

- Egy adott karakterlánc kulcsérték írása:

`dconf write {{/path/to/key}} "'{{string}}'"`

- Egy adott egész szám kulcsérték írása:

`dconf write {{/path/to/key}} "{{5}}"`

- Egy adott bólusú kulcsérték írása:

`dconf write {{/path/to/key}} "{{true|false}}"`

- Egy adott tömb kulcsérték írása:

`dconf write {{/path/to/key}} "[{{'first', 'second', ...}}]"`

- Egy adott üres tömb kulcsérték írása:

`dconf write {{/path/to/key}} "@as []"`
