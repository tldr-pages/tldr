# git clean

> Rimuovi i file non tracciati dall'albero di lavoro.
> Maggiori informazioni: <https://git-scm.com/docs/git-clean>.

- Rimuovi da Git i file non tracciati:

`git clean`

- Rimuovi in modo interattivo i file non tracciati:

`git clean -i`

- Mostra quali sono i file non tracciati che sarebbero rimossi, senza però rimuoverli davvero:

`git clean --dry-run`

- Forza la rimozione dei file non tracciati:

`git clean -f`

- Forza la rimozione delle cartelle non tracciate:

`git clean -fd`

- Rimuovi i file non tracciati, compresi quelli da ignorare elencati in `.gitignore` e `.git/info/exclude`:

`git clean -x`
