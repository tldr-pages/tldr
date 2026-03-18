# conda list

> Elenca i pacchetti installati in un ambiente conda.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/stable/commands/list.html>.

- Elenca tutti i pacchetti nell'ambiente attuale:

`conda list`

- Elenca i pacchetti in un ambiente specifico:

`conda list {{[-n|--name]}} {{ambiente}}`

- Elenca i pacchetti installati in un percorso specifico:

`conda list {{[-p|--prefix]}} {{percorso/all/ambiente}}`

- Filtra i pacchetti installati usando una `regex`:

`conda list {{regex}}`

- Esporta l'elenco dei pacchetti per usi futuri:

`conda list {{[-e|--export]}} > {{percorso/alla/lista-pacchetti.txt}}`
