# hg add

> Adaugă fișiere specificate în zona de așteptare pentru următoarea comite în Mercurial.
> Mai multe informaţii: <https://www.mercurial-scm.org/doc/hg.1.html#add>

- Adăugați fișiere sau directoare în zona de așteptare:

`hg add {{path/to/file}}`

- Adăugați toate fișierele neetajate care corespund unui model specificat:

`hg add --include {{pattern}}`

- Adăugați toate fișierele neetajate, excluzând cele care se potrivesc cu un model specificat:

`hg add --exclude {{pattern}}`

- Adăugarea recursivă a subdepozitelor:

`hg add --subrepos`

- Efectuați un test de executare fără a efectua nici o acțiune:

`hg add --dry-run`
