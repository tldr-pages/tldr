# cargo init

> Crée un nouveau paquet Cargo.
> Équivalent de `cargo new`, mais spécifier un répertoire est optionnel.
> Plus d'informations : <https://doc.rust-lang.org/cargo/commands/cargo-init.html>.

- Initialise un projet Rust binaire dans le répertoire actuel :

`cargo init`

- Initailise un projet de binaire Rust dans le répertoire spécifié :

`cargo init {{chemin/vers/répertoire}}`

- Initialise un projet de bibliothèque Rust dans le répertoire spécifié :

`cargo init --lib`

- Initialise un dépôt de système de gestion de version dans le répertoire du projet (défaut : `git`) :

`cargo init --vcs {{git|hg|pijul|fossil|none}}`

- Défini le nom du paquet (défaut : nom du répertoire) :

`cargo init --name {{nom_du_paquet}}`
