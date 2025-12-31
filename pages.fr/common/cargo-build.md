# cargo build

> Compile un paquet local et toutes ses dépendances.
> Plus d'informations : <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Compile un ou plusieurs paquets définis dans le manifeste `Cargo.toml` dans le dossier local :

`cargo {{[b|build]}}`

- Compile les artefacts avec le mode publication, avec des optimisations :

`cargo {{[b|build]}} {{[-r|--release]}}`

- Le fichier `Cargo.lock` doit être à jour :

`cargo {{[b|build]}} --locked`

- Compile tous les paquets de l'espace de travail :

`cargo {{[b|build]}} --workspace`

- Compile un paquet spécifique :

`cargo {{[b|build]}} {{[-p|--package]}} {{paquet}}`

- Compile uniquement le binaire spécifié :

`cargo {{[b|build]}} --bin {{nom_du_binaire}}`

- Compile uniquement le test cible spécifié :

`cargo {{[b|build]}} --test {{nom_du_test}}`
