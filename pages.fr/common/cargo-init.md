# cargo init

> Crée un nouveau paquet Cargo.
> Équivalent de `cargo new`, mais où spécifier un dossier est optionnel.
> Plus d'informations : <https://doc.rust-lang.org/cargo/commands/cargo-init.html>.

- Initilise un projet Rust binaire dans le dossier current :

`cargo init`

- Initilise un projet de binaire Rust dans le dossier spécifié :

`cargo init {{chemin/vers/dossier}}`

- Initialise un projet de bibliothèque Rust  dans le dossier spécifié :

`cargo init --lib`

- Initialise un dépot de système de gestion de version dans le dossier du projet (defaut : `git`) :

`cargo init --vcs {{git|hg|pijul|fossil|none}}`

- Défini le nom du paquet (defaut: nom du dossier):

`cargo init --name {{nom_du_paquet}}`
