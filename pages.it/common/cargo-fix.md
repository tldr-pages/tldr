# cargo fix

> Correggi automaticamente i warning dei lint segnalati da `rustc`.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-fix.html>.

- Correggi il codice anche se contiene già errori del compilatore:

`cargo fix --broken-code`

- Correggi il codice anche se la directory di lavoro ha modifiche non committate:

`cargo fix --allow-dirty`

- Migra un pacchetto alla prossima edition di Rust:

`cargo fix --edition`

- Correggi la libreria del pacchetto:

`cargo fix --lib`

- Correggi il test di integrazione specificato:

`cargo fix --test {{nome}}`

- Correggi tutti i membri dello workspace:

`cargo fix --workspace`
