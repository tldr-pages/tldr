# conda clean

> Elimina file temporanei o non utilizzati: cache degli indici, file di blocco, pacchetti inutilizzati, tarball e file di log.  
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/stable/commands/clean.html>.

- Elimina tutti i file temporanei o non utilizzati in modo dettagliato e conferma automaticamente tutte le richieste:

`conda clean {{[-avy|--all --verbose --yes]}}`

- Elimina solo la cache degli indici, i tarball e i file di log:

`conda clean {{[-itl|--index-cache --tarballs --logfiles]}}`

- Elimina solo i file temporanei di [c]ache che non potevano essere eliminati in precedenza perché in uso:

`conda clean {{[-c|--tempfiles]}} {{percorso/a/file_temporanei}}`

- Elimina solo i pacchetti non utilizzati. Potrebbe eliminare pacchetti installati con softlink:

`conda clean {{[-p|--packages]}}`

- Forza l'eliminazione di tutti i pacchetti scrivibili. È più esteso dell'opzione `--all`. Eliminerà anche i pacchetti installati con softlink:

`conda clean {{[-f|--force-pkgs-dirs]}}`

- Mostra l'aiuto:

`conda clean {{[-h|--help]}}`
