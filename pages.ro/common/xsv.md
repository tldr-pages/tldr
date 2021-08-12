# xsv

> Un set de instrumente pentru linia Către de comandă CSV scris în Rust.
> Mai multe informaţii: <https://github.com/BurntSushi/xsv>

- Inspectați anteturile unui fișier:

`xsv headers {{path/to/file.csv}}`

- Numără numărul de intrări:

`xsv count {{path/to/file.csv}}`

- Obțineți o prezentare generală a formei intrărilor:

`xsv stats {{path/to/file.csv}} | xsv table`

- Selectați câteva coloane:

`xsv select {{column_a,column_b}} {{path/to/file.csv}}`

- Arată 10 intrări aleatorii:

`xsv sample {{10}} {{path/to/file.csv}}`

- Alăturați-vă unei coloane dintr-un fișier în altul:

`xsv join --no-case {{column_a}} {{path/to/file/a.csv}} {{column_b}} {{path/to/file/b.csv}} | xsv table`
