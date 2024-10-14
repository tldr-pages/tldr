# cargo build

> Compile un paquet local et toutes ses dépendances.
> Plus d'informations : <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Compile un ou plusieurs paquets définis dans le manifeste `Cargo.toml` dans le dossier local :

`cargo build`

- Compile les artefacts avec le mode publication, avec des optimisations :

`cargo build --release`

- Le fichier `Cargo.lock` doit être à jour :

`cargo build --locked`

- Compile tous les paquets de l'espace de travail :

`cargo build --workspace`

- Compile un paquet spécifique :

`cargo build --package {{paquet}}`

- Compile uniquement le binaire spécifié :

`cargo build --bin {{nom_du_binaire}}`

- Compile uniquement le test cible spécifié :

`cargo build --test {{nom_du_test}}`
