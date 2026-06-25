# cargo tree

> Mostra una visualizzazione ad albero della dipendenza di un progetto.
> Nota: nell'albero, le dipendenze dei pacchetti contrassegnati con `(*)` sono già state mostrate altrove nel grafo, e quindi non sono ripetute.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-tree.html>.

- Mostra un albero delle dipendenze del progetto corrente:

`cargo tree`

- Mostra solo le dipendenze fino alla profondità specificata (es. quando `n` è 1 mostra solo le dipendenze dirette):

`cargo tree --depth {{n}}`

- Non visualizzare il pacchetto dato (e le sue dipendenze) nell'albero:

`cargo tree --prune {{package_spec}}`

- Mostra tutte le occorrenze delle dipendenze ripetute:

`cargo tree --no-dedupe`

- Mostra solo dipendenze normali/build/dev:

`cargo tree {{[-e|--edges]}} {{normal|build|dev}}`
