# csvsort

> Sortează fișierele CSV.
> Inclus în csvkit.
> Mai multe informaţii: <https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html>

- Sortați un fișier CSV după coloana 9:

`csvsort -c {{9}} {{data.csv}}`

- Sortați un fișier CSV după coloana „name” în ordine descrescătoare:

`csvsort -r -c {{name}} {{data.csv}}`

- Sortați un fișier CSV după coloana 2, apoi după coloana 4:

`csvsort -c {{2,4}} {{data.csv}}`

- Sortarea unui fişier CSV fără a deduce tipuri de date:

`csvsort --no-inference -c {{columns}} {{data.csv}}`
