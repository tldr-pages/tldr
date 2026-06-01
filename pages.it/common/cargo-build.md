# cargo build

> Compila un package locale e tutte le sue dipendenze.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Compila il package o i package definiti dal file manifesto `Cargo.toml` nel percorso locale:

`cargo {{[b|build]}}`

- Compila gli artifact in modalita' release, con ottimizzazioni:

`cargo {{[b|build]}} {{[-r|--release]}}`

- Richiede che `Cargo.lock` sia aggiornato:

`cargo {{[b|build]}} --locked`

- Compila tutti i package del workspace:

`cargo {{[b|build]}} --workspace`

- Compila un package specifico:

`cargo {{[b|build]}} {{[-p|--package]}} {{pacchetto}}`

- Compila solo il binario specificato:

`cargo {{[b|build]}} --bin {{nome}}`

- Compila solo il target di test specificato:

`cargo {{[b|build]}} --test {{test_name}}`