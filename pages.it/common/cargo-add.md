# cargo add

> Aggiungi dipendenze al manifesto `Cargo.toml` di un progetto Rust.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- Aggiungi la versione più recente di una dipendenza al progetto corrente:

`cargo add {{dependency}}`

- Aggiungi una versione specifica di una dipendenza:

`cargo add {{dependency}}@{{version}}`

- Aggiungi una dipendenza e abilita una o più feature specifiche:

`cargo add {{dependency}} {{[-F|--features]}} {{feature_1,feature_2,...}}`

- Aggiungi una dipendenza opzionale, che verrà esposta come feature del crate:

`cargo add {{dependency}} --optional`

- Aggiungi un crate locale come dipendenza:

`cargo add --path {{path/to/crate_directory}}`

- Aggiungi una dipendenza di sviluppo o di build:

`cargo add {{dependency}} --{{dev|build}}`

- Aggiungi una dipendenza disabilitando tutte le feature di default:

`cargo add {{dependency}} --no-default-features`
