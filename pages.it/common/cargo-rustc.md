# cargo rustc

> Compila un pacchetto Rust. Simile a `cargo build`, ma permette di passare opzioni aggiuntive al compilatore.
> Vedi `rustc --help` per tutte le opzioni disponibili.
> Vedi anche: `rustc`.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- Compila il pacchetto e passa opzioni a `rustc`:

`cargo rustc -- {{rustc_options}}`

- Compila gli artefatti in modalità release:

`cargo rustc {{[-r|--release]}}`

- Compila con ottimizzazioni specifiche per l'architettura della CPU corrente:

`cargo rustc {{[-r|--release]}} -- {{[-C|--codegen]}} target-cpu=native`

- Compila con ottimizzazioni per la velocità:

`cargo rustc -- {{[-C|--codegen]}} opt-level={{1|2|3}}`

- Compila con ottimizzazioni per la dimensione (`s` disattiva anche la vettorizzazione dei loop):

`cargo rustc -- {{[-C|--codegen]}} opt-level={{s|z}}`

- Controlla se il pacchetto utilizza codice `unsafe`:

`cargo rustc --lib -- -D unsafe-code`

- Compila un pacchetto specifico:

`cargo rustc {{[-p|--package]}} {{pacchetto}}`

- Compila solo il binario specificato:

`cargo rustc --bin {{nome}}`
