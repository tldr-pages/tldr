# git clean

> Eliminați fișierele neurmărite din arborele de lucru.
> Mai multe informaţii: <https://git-scm.com/docs/git-clean>

- Ștergeți fișierele care nu sunt urmărite de Git:

`git clean`

- Ștergeți interactiv fișierele care nu sunt urmărite de Git:

`git clean -i`

- Afișați ce fișiere ar fi șterse fără a le șterge efectiv:

`git clean --dry-run`

- Ștergeți cu forța fișierele care nu sunt urmărite de Git:

`git clean -f`

- Ștergeți forțat directoarele care nu sunt urmărite de Git:

`git clean -fd`

- Ștergeți fișierele neurmărite, inclusiv fișierele ignorate în `.gitignore` și `.git/info/exclude`:

`git clean -x`
