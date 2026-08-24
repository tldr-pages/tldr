# cargo rustdoc

> Costruisci la documentazione dei pacchetti Rust.
> Simile a `cargo doc`, ma permette di passare opzioni a `rustdoc`. Vedi `rustdoc --help` per tutte le opzioni disponibili.
> Vedi anche: `rustdoc`.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>.

- Passa opzioni a `rustdoc`:

`cargo rustdoc -- {{rustdoc_options}}`

- Segnala un lint della documentazione:

`cargo rustdoc -- {{[-W|--warn]}} rustdoc::{{lint_name}}`

- Ignora un lint della documentazione:

`cargo rustdoc -- {{[-A|--allow]}} rustdoc::{{lint_name}}`

- Documenta la libreria del pacchetto:

`cargo rustdoc --lib`

- Documenta il binario specificato:

`cargo rustdoc --bin {{nome}}`

- Documenta l'example specificato:

`cargo rustdoc --example {{nome}}`

- Documenta il test di integrazione specificato:

`cargo rustdoc --test {{nome}}`
