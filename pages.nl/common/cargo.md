# cargo

> Beheer Rust projecten en hun afhankelijkheden (crates).
> Sommige subcommando's zoals `build` hebben een eigen documentatie pagina.
> Meer informatie: <https://doc.rust-lang.org/cargo>.

- Zoek naar crates:

`cargo search {{zoekopdracht}}`

- Installeer een crate:

`cargo install {{crate-naam}}`

- Geef een lijst van geïnstalleerde crates:

`cargo install --list`

- Maak een nieuwe Rust-binary (bin) of -bibliotheek (lib) in de gegeven map. (Standaard is de huidige map):

`cargo init --{{bin|lib}} {{pad/naar/map}}`

- Voeg een afhankelijkheid toe aan `Cargo.toml` in de huidge map:

`cargo add {{afhankelijkheid}}`

- Bouw het Rust-project in de huidige map door gebruik te maken van het release-profiel:

`cargo build --release`

- Bouw het Rust-project in de huidige map door gebruik te maken van de nachtelijkse compiler (vereist `rustup`):

`cargo +nightly build`

- Bouw met een gegeven aantal taken. (Standaard is het aantal CPU-kernen):

`cargo build --jobs {{aantal_taken}}`
