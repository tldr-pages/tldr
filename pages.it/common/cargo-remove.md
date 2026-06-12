# cargo remove

> Rimuovi dipendenze dal manifesto `Cargo.toml` di un progetto Rust.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-remove.html>.

- Rimuovi una dipendenza dal progetto corrente:

`cargo remove {{dipendenza}}`

- Rimuovi una dipendenza di sviluppo o di build:

`cargo remove --{{dev|build}} {{dipendenza}}`

- Rimuovi una dipendenza per la piattaforma target specificata:

`cargo remove --target {{target}} {{dipendenza}}`
