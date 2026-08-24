# cargo run

> Esegui il pacchetto Cargo corrente.
> Nota: la directory di lavoro dell'eseguibile sarà impostata sulla directory di lavoro corrente.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-run.html>.

- Esegui il target binario predefinito:

`cargo {{[r|run]}}`

- Esegui il binario specificato:

`cargo {{[r|run]}} --bin {{nome}}`

- Esegui l'example specificato:

`cargo {{[r|run]}} --example {{nome}}`

- Attiva una lista di feature separate da spazio o virgola:

`cargo {{[r|run]}} {{[-F|--features]}} "{{feature1 feature2 ...}}"`

- Disabilita le feature di default:

`cargo {{[r|run]}} --no-default-features`

- Attiva tutte le feature disponibili:

`cargo {{[r|run]}} --all-features`

- Esegui con il profilo specificato:

`cargo {{[r|run]}} --profile {{nome}}`
