# cargo build

> Compila un pacchetto locale e tutte le sue dipendenze.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Compila il pacchetto o i pacchetti definiti dal manifesto `Cargo.toml` nella directory locale:

`cargo {{[b|build]}}`

- Compila gli artefatti in modalità release, con ottimizzazioni:

`cargo {{[b|build]}} {{[-r|--release]}}`

- Richiedi che `Cargo.lock` sia aggiornato:

`cargo {{[b|build]}} --locked`

- Compila tutti i pacchetti nello workspace:

`cargo {{[b|build]}} --workspace`

- Compila un pacchetto specifico:

`cargo {{[b|build]}} {{[-p|--package]}} {{package}}`

- Compila solo il binario specificato:

`cargo {{[b|build]}} --bin {{name}}`

- Compila solo il test target specificato:

`cargo {{[b|build]}} --test {{test_name}}`
