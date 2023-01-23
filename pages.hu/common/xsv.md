# xsv

> Rust nyelven írt CSV parancssori eszközkészlet. További információ: <https://github.com/BurntSushi/xsv>.

- Egy fájl fejlécének vizsgálata:

`xsv headers {{path/to/file.csv}}`

- Számolja meg a bejegyzések számát:

`xsv count {{path/to/file.csv}}`

- Áttekintést kaphat a bejegyzések alakjáról:

`xsv stats {{path/to/file.csv}} | xsv table`

- Válasszon ki néhány oszlopot:

`xsv select {{column_a,column_b}} {{path/to/file.csv}}`

- Mutasson meg 10 véletlenszerű bejegyzést:

`xsv sample {{10}} {{path/to/file.csv}}`

- Egy oszlop összekapcsolása az egyik fájlból a másikba:

`xsv join --no-case {{column_a}} {{path/to/file/a.csv}} {{column_b}} {{path/to/file/b.csv}} | xsv table`
