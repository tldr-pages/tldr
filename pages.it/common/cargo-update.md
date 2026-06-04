# cargo update

> Aggiorna le dipendenze come registrate in `Cargo.lock`.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-update.html>.

- Aggiorna le dipendenze in `Cargo.lock` all'ultima versione possibile:

`cargo update`

- Mostra cosa verrebbe aggiornato, senza scrivere effettivamente il lockfile:

`cargo update {{[-n|--dry-run]}}`

- Aggiorna solo le dipendenze specificate:

`cargo update --package {{dipendenza1}} --package {{dipendenza2}} --package {{dipendenza3}}`

- Imposta una dipendenza specifica a una versione precisa:

`cargo update --package {{dipendenza}} --precise {{1.2.3}}`
