# pixterm

> Képnyomtatás a terminálban Lásd még: `chafa`, `catimg`. További információ: [https://github.com/eliukblau/pixterm.](https://github.com/eliukblau/pixterm)

- Statikus kép renderelése közvetlenül a terminálban:

`pixterm {{path/to/file}}`

- A kép eredeti képarányának használata:

`pixterm -s 2 {{path/to/file}}`

- Egyéni képarány megadása a \[t\]erminális \[r\]sorok és \[c\]oszlopok meghatározott számával:

`pixterm -tr {{24}} -tc {{80}} {{path/to/file}}`

- A kimenet szűrése \[m\]atte háttérszínnel és karakter \[d\]itheringgel:

`pixterm -m {{000000}} -d 2 {{path/to/file}}`
