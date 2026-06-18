# cargo binstall

> Installa binari Rust da artifact CI.
> In mancanza di binari disponibili, esegue il fallback su `cargo install` (da sorgente).
> Nota: questo non è un comando integrato di Cargo; va installato separatamente.
> Maggiori informazioni: <https://github.com/cargo-bins/cargo-binstall>.

- Installa un pacchetto da <https://crates.io>:

`cargo binstall {{pacchetto}}`

- Installa una versione specifica di un pacchetto (di default l'ultima):

`cargo binstall {{pacchetto}}@{{versione}}`

- Installa un pacchetto disabilitando i prompt di conferma:

`cargo binstall {{[-y|--no-confirm]}} {{pacchetto}}`
