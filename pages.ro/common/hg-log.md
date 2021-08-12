# hg log

> Afișează istoricul revizuirii depozitului.
> Mai multe informaţii: <https://www.mercurial-scm.org/doc/hg.1.html#log>

- Afișează întregul istoric al revizuirii depozitului:

`hg log`

- Afișează istoricul revizuirii cu un grafic ASCII:

`hg log --graph`

- Afișați istoricul revizuirii cu nume de fișiere care corespund unui model specificat:

`hg log --include {{pattern}}`

- Afișează istoricul revizuirii, excluzând numele fișierelor care se potrivesc cu un model specificat:

`hg log --exclude {{pattern}}`

- Afișează informațiile din jurnal pentru o anumită revizuire:

`hg log --rev {{revision}}`

- Afișează istoricul revizuirii pentru o anumită ramură:

`hg log --branch {{branch}}`

- Afișează istoricul revizuirii pentru o anumită dată:

`hg log --date {{date}}`

- Afișează revizuirile comise de un anumit utilizator:

`hg log --user {{user}}`
