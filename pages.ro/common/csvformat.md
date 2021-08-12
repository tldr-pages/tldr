# csvformat

> Conversia unui fişier CSV la un format de ieşire particularizat.
> Inclus în csvkit.
> Mai multe informaţii: <https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html>

- Conversia la un fișier delimitat tab-( TSV):

`csvformat -T {{data.csv}}`

- Conversia delimitatorilor la un caracter personalizat:

`csvformat -D "{{custom_character}}" {{data.csv}}`

- Conversia terminațiilor de linie în retur de transport (^M) + linie de alimentare:

`csvformat -M "{{\r\n}}" {{data.csv}}`

- Minimizarea utilizării caracterelor citat

`csvformat -U 0 {{data.csv}}`

- Maximizarea utilizării caracterelor citat:

`csvformat -U 1 {{data.csv}}`
