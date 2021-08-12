# grex

> Simplu instrument de linie de comandă pentru a genera expresii regulate.
> Mai multe informaţii: <https://github.com/pemistahl/grex>

- Generează o expresie regulată simplă:

` grex {{space_separated_strings}}`

- Generați o expresie regulată insensibilă la minuscule:

`grex -i {{space_separated_strings}}`

- Înlocuiți cifrele cu „\ d”:

`grex -d {{space_separated_strings}}`

- Înlocuiți caracterul cuvintelor Unicode cu '\ w':

`grex -w {{space_separated_strings}}`

- Înlocuiți spațiile cu '\ s':

`grex -s {{space_separated_strings}}`

- Adaugă reprezentare cuantificator {min, max} pentru repetarea sub-stringurilor:

`grex -r {{space_separated_strings}}`
