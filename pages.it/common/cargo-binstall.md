# cargo binstall

> Installa binari Rust da artifact CI.
> Ricorre a `cargo install` (dal codice sorgente) se non sono disponibili binari.
> Nota: non e' un comando Cargo integrato, va installato prima.
> More information: <https://github.com/cargo-bins/cargo-binstall>.

- Installa un package da <https://crates.io>:

`cargo binstall {{pacchetto}}`

- Installa una versione specifica di un package (di default l'ultima):

`cargo binstall {{pacchetto}}@{{versione}}`

- Installa un package e disabilita le richieste di conferma:

`cargo binstall {{[-y|--no-confirm]}} {{pacchetto}}`