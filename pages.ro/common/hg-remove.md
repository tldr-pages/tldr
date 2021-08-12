# hg remove

> Eliminați fișierele specificate din zona de așteptare.
> Mai multe informaţii: <https://www.mercurial-scm.org/doc/hg.1.html#remove>

- Eliminați fișierele sau directoarele din zona de așteptare:

`hg remove {{path/to/file}}`

- Eliminați toate fișierele pe etape care se potrivesc cu un model specificat:

`hg remove --include {{pattern}}`

- Eliminați toate fișierele în etape, excluzând cele care se potrivesc cu un model specificat:

`hg remove --exclude {{pattern}}`

- Eliminarea recursivă a subdepozitelor:

`hg remove --subrepos`

- Eliminați fișierele din depozit care au fost eliminate fizic:

`hg remove --after`
