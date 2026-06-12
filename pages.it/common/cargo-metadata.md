# cargo metadata

> Stampa i membri del workspace e le dipendenze risolte del pacchetto corrente in formato JSON.
> Nota: il formato di output potrebbe cambiare in versioni future di Cargo.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-metadata.html>.

- Stampa i membri del workspace e le dipendenze risolte del pacchetto corrente:

`cargo metadata`

- Stampa solo i membri del workspace senza recuperare le dipendenze:

`cargo metadata --no-deps`

- Stampa i metadata in un formato specifico basato sulla versione specificata:

`cargo metadata --format-version {{versione}}`

- Stampa i metadata con il campo `resolve` includendo le dipendenze solo per il target dato (Nota: l'array `packages` continuerà ad includere le dipendenze per tutti i target):

`cargo metadata --filter-platform {{target_triple}}`
