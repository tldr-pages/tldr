# jtbl

> Utilitate pentru a imprima datele JSON și JSON Lines ca tabel în terminal.
> Mai multe informaţii: <https://github.com/kellyjonbrazil/jtbl>

- Imprimați un tabel de intrare JSON sau JSON Lines:

`cat {{file.json}} | jtbl`

- Imprimați un tabel și specificați lățimea coloanei pentru ambalare:

`cat {{file.json}} | jtbl --cols={{width}}`

- Imprimați un tabel și trunchiați rânduri în loc de ambalaj:

`cat {{file.json}} | jtbl -t`

- Imprimați un tabel și nu înfășurați sau trunchiați rânduri:

`cat {{file.json}} | jtbl -n`
