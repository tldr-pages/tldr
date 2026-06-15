# cargo doc

> Costruisci la documentazione dei pacchetti Rust.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Costruisci la documentazione per il progetto corrente e tutte le dipendenze:

`cargo {{[d|doc]}}`

- Non costruire la documentazione per le dipendenze:

`cargo {{[d|doc]}} --no-deps`

- Costruisci e apri la documentazione in un browser:

`cargo {{[d|doc]}} --open`

- Costruisci e visualizza la documentazione di un pacchetto specifico:

`cargo {{[d|doc]}} --open {{[-p|--package]}} {{package}}`
