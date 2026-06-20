# cargo publish

> Carica un pacchetto su un registro.
> Nota: devi aggiungere un token di autenticazione con `cargo login` prima di pubblicare un pacchetto.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-publish.html>.

- Esegui i controlli, crea un file `.crate` e caricalo sul registro:

`cargo publish`

- Esegui i controlli, crea un file `.crate` ma non caricarlo (equivalente a `cargo package`):

`cargo publish {{[-n|--dry-run]}}`

- Usa il registro specificato (i nomi dei registri possono essere definiti nella configurazione - il predefinito è <https://crates.io>):

`cargo publish --registry {{nome}}`
