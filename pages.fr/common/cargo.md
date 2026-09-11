# cargo

> Gestion d'un projet Rust et ses dépendences (crates).
> Certaines sous-commandes comme `build` ont leur propre documentation.
> Plus d'informations : <https://doc.rust-lang.org/stable/cargo/>.

- Recherche des crates :

`cargo search {{recherche}}`

- Installe un crate :

`cargo install {{nom_du_crate}}`

- Liste les crates déjà installés :

`cargo install --list`

- Crée un nouveau binaire ou librairie du projet Rust dans les répertoires spécifiés (ou dans le répertoire courant par défaut) :

`cargo init --{{bin|lib}} {{chemin/vers/répertoire}}`

- Ajoute une dépendance à `Cargo.toml` dans le répertoire actuel :

`cargo add {{dépendance}}`

- Compile le projet Rust dans le dossier courant en utilisant le profil release :

`cargo {{[b|build]}} {{[-r|--release]}}`

- Exécute le binaire compilé (le compile s’il ne l’est pas déjà) :

`cargo {{[r|run]}}`

- Compile le projet Rust dans le dossier courant en utilisant le compilateur nightly :

`cargo +nightly {{[b|build]}}`
