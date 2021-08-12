# gopass

> Manager de parole standard Unix pentru echipe. Scris în Go.
> Mai multe informaţii: <https://www.gopass.pw>

- Iniţializaţi setările de configurare:

`gopass init`

- Creați o nouă intrare:

`gopass new`

- Arată toate magazinele:

`gopass mounts`

- Montați un magazin comun Git:

`gopass mounts add {{store_name}} {{git_repo_url}}`

- Căutare interactivă folosind un cuvânt cheie:

`gopass show {{keyword}}`

- Căutare folosind un cuvânt cheie:

`gopass find {{keyword}}`

- Sincronizează toate magazinele montate:

`gopass sync`

- Afișează o anumită intrare de parolă:

`gopass {{store_name|path/to/directory|email@email.com}}`
