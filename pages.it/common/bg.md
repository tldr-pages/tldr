# bg

> Riprende job che sono stati sospesi (e.g. usando `<Ctrl z>`) mettendoli in esecuzione in background.
> Maggiori informazioni: <https://www.gnu.org/software/bash/manual/bash.html#index-bg>.

- Riprendi il job sospeso più recentemente ed eseguilo in background:

`bg`

- Riprendi uno specifico job (usa `jobs -l` per trovare l'ID) ed eseguilo in background:

`bg %{{id_job}}`
