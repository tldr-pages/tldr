# cargo add

> Ajoute des dépendences au manifeste `Cargo.toml` d'un projet Rust.
> Plus d'informations : <https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- Ajoute la dernière version d'une dépendance au projet courant :

`cargo add {{dépendance}}`

- Ajoute une version spécifique d'une dépendance :

`cargo add {{dépendance}}@{{version}}`

- Ajoute une dépendance et active une ou plusieures fonctionnalités :

`cargo add {{dépendance}} --features {{fonctionnalité_1}},{{fonctionnalité_2}}`

- Ajoute une dépendance optionnelle, qui sera exposée comme une fonctionnalité du crate :

`cargo add {{dépendance}} --optional`

- Ajoute un crate local en tant que dépendance :

`cargo add --path {{chemin/vers/crate}}`

- Ajoute une dépendance de développement ou de compilation :

`cargo add {{dépendance}} --{{dev|build}}`

- Ajoute une dépendance avec toutes les fonctionnalités par défaut désactivées :

`cargo add {{dépendance}} --no-default-features`
