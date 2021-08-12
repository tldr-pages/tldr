# hg clone

> Creați o copie a unui depozit existent într-un director nou.
> Mai multe informaţii: <https://www.mercurial-scm.org/doc/hg.1.html#clone>

- Clonează un depozit într-un director specificat:

`hg clone {{remote_repository_source}} {{destination_path}}`

- Clona un depozit la capul unei ramuri specifice, ignorând mai târziu comite:

`hg clone --branch {{branch}} {{remote_repository_source}}`

- Clonează un depozit cu doar directorul `.hg `, fără a verifica fișierele:

`hg clone --noupdate {{remote_repository_source}}`

- Clonează un depozit la o anumită revizuire, etichetă sau sucursală, păstrând întregul istoric:

`hg clone --updaterev {{revision}} {{remote_repository_source}}`

- Clona un depozit până la o revizuire specifică, fără nici un istoric mai nou:

`hg clone --rev {{revision}} {{remote_repository_source}}`
