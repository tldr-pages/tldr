# cargo add
> Aggiunge dipendenze al manifest `Cargo.toml` di un progetto Rust.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- Aggiunge la versione più recente di una dipendenza al progetto corrente:
`cargo add {{dipendenza}}`

- Aggiunge una versione specifica di una dipendenza:
`cargo add {{dipendenza}}@{{versione}}`

- Aggiunge una dipendenza e abilita una o più feature specifiche:
`cargo add {{dipendenza}} {{[-F|--features]}} {{feature_1,feature_2,...}}`

- Aggiunge una dipendenza opzionale, esposta poi come feature del crate:
`cargo add {{dipendenza}} --optional`

- Aggiunge un crate locale come dipendenza:
`cargo add --path {{percorso/del/crate}}`

- Aggiunge una dipendenza di sviluppo o di build:
`cargo add {{dipendenza}} --{{dev|build}}`

- Aggiunge una dipendenza con tutte le feature predefinite disabilitate:
`cargo add {{dipendenza}} --no-default-features`