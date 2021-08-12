# hg commit

> Comite toate fișierele în etape sau specificate în depozit.
> Mai multe informaţii: <https://www.mercurial-scm.org/doc/hg.1.html#commit>

- Comite fișiere pe etape la depozit:

`hg commit`

- Comite un anumit fișier sau director:

`hg commit {{path/to/file_or_directory}}`

- Comite cu un mesaj specific:

`hg commit --message {{message}}`

- Comite toate fișierele care corespund unui model specificat:

`hg commit --include {{pattern}}`

- Comite toate fișierele, cu excepția celor care se potrivesc cu un model specificat:

`hg commit --exclude {{pattern}}`

- Comite folosind modul interactiv:

`hg commit --interactive`
