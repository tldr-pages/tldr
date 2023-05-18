# cargo

> Rust pakketbeheerder.
> Beheer Rust projecten en hun afhankelijkheden (crates).
> Meer informatie: <https://doc.rust-lang.org/cargo>.

- Zoek naar crates:

`cargo search {{zoekopdracht}}`

- Installeer een crate:

`cargo install {{crate-naam}}`

- Geef een lijst van geïnstalleerde crates:

`cargo install --list`

- Maak een nieuwe Rust-binary (bin) of -bibliotheek (lib) in de huidige map:

`cargo init --{{bin|lib}}`

- Maak een nieuwe Rust-binary (bin) of -bibliotheek (lib) in de gegeven map:

`cargo new {{pad/naar/map}} --{{bin|lib}}`

- Bouw het Rust-project in de huidige map:

`cargo build`

- Bouw met een gegeven aantal taken. (Standaard is het aantal CPU-kernen):

`cargo build --jobs {{aantal_taken}}`
