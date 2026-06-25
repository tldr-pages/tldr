# cargo owner

> Gestisci i maintainer (owner) di un crate sul registro.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-owner.html>.

- Invita l'utente o il team indicato come owner:

`cargo owner {{[-a|--add]}} {{username|github:org_name:team_name}} {{crate}}`

- Rimuovi l'utente o il team indicato come owner:

`cargo owner {{[-r|--remove]}} {{username|github:org_name:team_name}} {{crate}}`

- Elenca gli owner di un crate:

`cargo owner {{[-l|--list]}} {{crate}}`

- Usa il registro specificato (i nomi dei registri possono essere definiti nella configurazione - il predefinito è <https://crates.io>):

`cargo owner --registry {{nome}}`
