# conda clean

> Elimina file temporanei/inutilizzati: cache indice, lock, pacchetti, tarball, log.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/stable/commands/clean.html>.

- Elimina tutto verbosamente (sì a tutto):

`conda clean {{[-avy|--all --verbose --yes]}}`

- Elimina solo cache indice, tarball, log:

`conda clean {{[-itl|--index-cache --tarballs --logfiles]}}`

- Elimina cache temporanei bloccati:

`conda clean {{[-c|--tempfiles]}}`

- Elimina pacchetti inutilizzati:

`conda clean {{[-p|--packages]}}`

- Forza eliminazione tutti pacchetti scrivibili:

`conda clean {{[-f|--force-pkgs-dirs]}}`

- Aiuto:

`conda clean {{[-h|--help]}}`
