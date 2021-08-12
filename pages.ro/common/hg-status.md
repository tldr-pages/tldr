# hg status

> Afișați fișierele care s-au modificat în directorul de lucru.
> Mai multe informaţii: <https://www.mercurial-scm.org/doc/hg.1.html#status>

- Afișați starea fișierelor modificate:

`hg status`

- Afișează numai fișierele modificate:

`hg status --modified`

- Afișează numai fișierele adăugate:

`hg status --added`

- Afișează numai fișierele eliminate:

`hg status --removed`

- Afișează numai fișierele șterse (dar urmărite):

`hg status --deleted`

- Afișează modificările în directorul de lucru în comparație cu un set de modificări specificat:

`hg status --rev {{revision}}`

- Afișează numai fișiere care corespund unui model glob specificat:

`hg status --include {{pattern}}`

- Afișați fișiere, excluzând cele care se potrivesc cu un model glob specificat:

`hg status --exclude {{pattern}}`
