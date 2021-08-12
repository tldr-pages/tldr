# history

> Istoricul liniei de comandă.
> Mai multe informaţii: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>

- Afișează lista istoricului comenzilor cu numere de linie:

`history`

- Afișează ultimele 20 de comenzi (în `zsh` afișează toate comenzile pornind de la 20):

`history {{20}}`

- Ștergeți lista istoricului comenzilor (numai pentru shell-ul curent `bash`):

`history -c`

- Suprascrie fișierul istoric cu istoricul shell-ului curent `bash` (adesea combinat cu `istorie -c` la istoricul de purjare):

`history -w`

- Ștergeți intrarea din istoric la decalajul specificat:

`history -d {{offset}}`
