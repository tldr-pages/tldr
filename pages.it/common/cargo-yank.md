# cargo yank

> Rimuovi un crate pubblicato dall'indice. Questo dovrebbe essere usato solo quando hai pubblicato accidentalmente una versione gravemente difettosa.
> Nota: questo non rimuove alcun dato. Il crate rimane disponibile dopo uno yank — questo impedisce solo che nuovi progetti lo usino.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-yank.html>.

- Rimuovi la versione specificata di un crate dall'indice:

`cargo yank {{crate}}@{{versione}}`

- Annulla uno yank (cioè permetti di scaricarlo di nuovo):

`cargo yank --undo {{crate}}@{{versione}}`

- Usa il registro specificato (i nomi dei registri possono essere definiti nella configurazione - il predefinito è <https://crates.io>):

`cargo yank --registry {{nome}} {{crate}}@{{versione}}`
