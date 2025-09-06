# cargo

> Gestion d'un projet Rust et ses dependences (crates).
> Certaines sous-commandes comme `build` ont leurs propres documentations.
> Plus d'informations : <https://doc.rust-lang.org/cargo>.

- Rechercher des crates :

`cargo search {{recherche}}`

- Installer un crate :

`cargo install {{nom_du_crate}}`

- Lister les crates déjà installés :

`cargo install --list`

- Crée un nouveau binaire ou librairie du projet Rust dans les dossiers spécifiés (ou dans le dossier courant par défaut) :

`cargo init --{{bin|lib}} {{chemin/vers/dossier}}`

- Compile le projet Rust dans le dossier courant en utilisant le profil release :

`cargo {{[b|build]}} {{[-r|--release]}}`

- Compiler le projet Rust dans le dossier courant en utilisant le compilateur nightly :

`cargo +nightly {{[b|build]}}`

- Compiler en utilisant un nombre spécifique de threads (par défaut on prend le nombre de coeurs du CPU) :

`cargo {{[b|build]}} --jobs {{nombre_de_threads}}`
