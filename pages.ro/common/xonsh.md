# xonsh

> Python-alimentat, cross-platform, Unix-gazing shell.
> Scrieți și amestecați codul SH/Python în Xonsh (scoică pronunțată).
> Mai multe informaţii: <https://xon.sh>

- Începeți o sesiune de shell interactivă:

`xonsh`

- Executați o singură comandă și apoi ieșiți:

`xonsh -c "{{command}}"`

- Rulați comenzi dintr-un fișier script și apoi ieșiți:

`xonsh {{path/to/script_file.xonsh}}`

- Definirea variabilelor de mediu pentru procesul de shell:

`xonsh -D{{name1}}={{value1}} -D{{name2}}={{value2}}`

- Încărcați fișierele de configurare `.xonsh` sau `.json` specificate:

`xonsh --rc {{path/to/file1.xonsh}} {{path/to/file2.json}}`

- Omite încărcarea fişierului de configurare `.xonshrc`:

`xonsh --no-rc`
