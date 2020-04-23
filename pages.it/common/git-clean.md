# git clean

> Elimina i file non tracciati dall'albero di lavoro.
> Maggiori informazioni: <https://git-scm.com/docs/git-clean>.

- Elimina i file che non sono tracciati da git:

`git clean`

- Elimina in modo interattivo i file non tracciati da git:

`git clean -i`

- Mostra quali file non tracciati sarebbero eliminati, senza però eliminarli davvero:

`git clean --dry-run`

- Forza l'eliminazione dei file non tracciati da git:

`git clean -f`

- Forza l'eliminazione delle cartelle non tracciate da git:

`git clean -fd`

- Elimina i file non tracciati, compresi quelli da ignorare elencati in `.gitignore` e `.git/info/exclude`:

`git clean -x`
