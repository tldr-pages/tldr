# cargo clippy

> Una raccolta di lint per catturare errori comuni e migliorare il codice Rust.
> Maggiori informazioni: <https://github.com/rust-lang/rust-clippy>.

- Esegui i controlli sul codice nella directory corrente:

`cargo clippy`

- Richiedi che `Cargo.lock` sia aggiornato:

`cargo clippy --locked`

- Esegui i controlli su tutti i pacchetti nello workspace:

`cargo clippy --workspace`

- Esegui i controlli per un pacchetto:

`cargo clippy --package {{package}}`

- Esegui i controlli per un gruppo di lint (vedi <https://rust-lang.github.io/rust-clippy/stable/index.html#?groups=cargo,complexity,correctness,deprecated,nursery,pedantic,perf,restriction,style,suspicious>):

`cargo clippy -- {{[-W|--warn]}} clippy::{{lint_group}}`

- Tratta i warning come errori:

`cargo clippy -- {{[-D|--deny]}} warnings`

- Esegui i controlli ignorando i warning:

`cargo clippy -- {{[-A|--allow]}} warnings`

- Applica automaticamente i suggerimenti di Clippy:

`cargo clippy --fix`
