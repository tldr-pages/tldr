# grep

> Găsiți modele în fișiere utilizând expresii regulate.
> Mai multe informaţii: <https://www.gnu.org/software/grep/manual/grep.html>

- Căutați un model într-un fișier:

`grep "{{search_pattern}}" {{path/to/file}}`

- Căutați un șir exact (dezactivează expresiile regulate):

`grep --fixed-strings "{{exact_string}}" {{path/to/file}}`

- Căutați un model în toate fișierele recursiv într-un director, afișând numerele de linie de potriviri, ignorând fișierele binare:

`grep --recursive --line-number --binary-files={{without-match}} "{{search_pattern}}" {{path/to/directory}}`

- Utilizați expresii regulate extinse (suporturi `? `, `+`,` {} `,` () `și `|`), în modul insensibil la litere mici și mici:

`grep --extended-regexp --ignore-case "{{search_pattern}}" {{path/to/file}}`

- Imprimați 3 linii de context în jurul, înainte sau după fiecare meci:

`grep --{{context|before-context|after-context}}={{3}} "{{search_pattern}}" {{path/to/file}}`

- Imprimați numele fișierului și numărul liniei pentru fiecare meci:

`grep --with-filename --line-number "{{search_pattern}}" {{path/to/file}}`

- Căutați linii care se potrivesc unui model, tipăriți numai textul potrivit:

`grep --only-matching "{{search_pattern}}" {{path/to/file}}`

- Căutare stdin pentru linii care nu se potrivesc cu un model:

`cat {{path/to/file}} | grep --invert-match "{{search_pattern}}"`
