# csvkit

> Setul de instrumente de manipulare pentru fişiere CSV.
> Vezi comenzile individuale: `csvclean`, `csvcut`, `csvformat`, `csvgrep`, `csvlook`, `csvpy`, `csvsort`, `csvstat`.
> Mai multe informaţii: <https://csvkit.readthedocs.io/en/0.9.1/cli.html>

- Rulați o comandă într-un fișier CSV cu un delimitator personalizat:

`{{cmd}} -d {{delimiter}} {{filename.csv}}`

- Rulați o comandă într-un fișier CSV cu o filă ca delimitator (suprascrie -d):

`{{cmd}} -t {{filename.csv}}`

- Rulați o comandă pe un fișier CSV cu un caracter de citat personalizat:

`{{cmd}} -q {{quote_char}} {{filename.csv}}`

- Rulați o comandă într-un fișier CSV fără rând antet:

`{{cmd}} -H {{filename.csv}}`
