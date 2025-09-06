# git prune

> Elimina dal database degli oggetti quelli non più raggiungibili.
> Questo comando è usato più spesso internamente da Git gc piuttosto che in modo diretto.
> Maggiori informazioni: <https://git-scm.com/docs/git-prune>.

- Elenca quali oggetti saranno eliminati da Git prune senza eliminarli definitivamente:

`git prune --dry-run`

- Elimina gli oggetti non raggiungibili e stampane un elenco su `stdout`:

`git prune --verbose`

- Elimina gli oggetti non raggiungibili, mostrando lo stato di avanzamento:

`git prune --progress`
