# ls

> Afișează conținutul unui folder.
> Mai multe informații: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- Afișează fișierele câte unul pe linie:

`ls -1`

- Afișează toate fișierele, inclusiv cele ascunse:

`ls {{[-a|--all]}}`

- Afișează fișierele cu un simbol la final pentru a indica tipul (folder/, link_simbolic@, executabil*, ...):

`ls {{[-F|--classify]}}`

- Afișează toate fișierele în format [l]ung (permisiuni, proprietar, dimensiune și data modificării):

`ls {{[-la|-l --all]}}`

- Afișează fișierele în format [l]ung cu dimensiunile în unități citibile (KiB, MiB, GiB):

`ls {{[-lh|-l --human-readable]}}`

- Afișează fișierele în format [l]ung, sortate descrescător după dimensiune ([S]ize), recursiv:

`ls {{[-lSR|-lS --recursive]}}`

- Afișează fișierele în format [l]ung, sortate după [t]impul modificării și în ordine inversă (cele mai vechi primele):

`ls {{[-ltr|-lt --reverse]}}`

- Afișează doar folderele:

`ls {{[-d|--directory]}} */`
