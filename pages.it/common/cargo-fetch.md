# cargo fetch

> Recupera le dipendenze di un pacchetto dalla rete.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-fetch.html>.

- Recupera le dipendenze specificate in `Cargo.lock` (per tutti i target):

`cargo fetch`

- Recupera le dipendenze per il target specificato:

`cargo fetch --target {{target_triple}}`
