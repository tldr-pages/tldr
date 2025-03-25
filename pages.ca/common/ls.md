# ls

> Llista els continguts d'un directori.
> Més informació: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- Llista els fitxers un per línia:

`ls -1`

- Llista tots els fitxers, incloent els ocults:

`ls {{[-a|--all]}}`

- Llista tots els fitxers, afegint `/` al nom dels directoris:

`ls {{[-F|--classify]}}`

- Llista de format llarg (permisos, propietat, mida i data de modificació) de tots els fitxers:

`ls {{[-la|--all -l]}}`

- Llista de format llarg amb unitats llegibles per humans (KiB, MiB, GiB):

`ls {{[-lh|-l --human-readable]}}`

- Llista de format lalrg ordenat per mida (descendent):

`ls {{-lSR|-lS --recursive}}`

- Llista de format llarg de tots els fitxers, organitzat per data de modificació (més antics primer):

`ls {{[-ltr|-lt --reverse]}}`

- Llista només directoris:

`ls {{[-d|--directory]}} */`
