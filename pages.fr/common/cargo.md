# cargo

> Gestion d'un projet Rust et ses dependences (crates).
> Certaines sous-commandes comme `cargo build` ont leurs propres documentations.
> Plus d'informations : <https://crates.io>.

- Rechercher des crates :

`cargo search {{recherche}}`

- Installer un crate :

`cargo install {{nom_du_crate}}`

- Lister les crates déjà installés :

`cargo install --list`

- Créer un nouveau binaire ou librairie du projet Rust dans le dossier courant :

`cargo init --{{bin|lib}}`

- Créer un nouveau binaire ou librairie du projet Rust dans un dossier spécifique :

`cargo new {{chemin/vers/dossier}} --{{bin|lib}}`

- Compiler le projet Rust dans le dossier courant :

`cargo build`

- Compiler le projet Rust dans le dossier courant en utilisant le compilateur nightly :

`cargo +nightly build`

- Compiler en utilisant un nombre spécifique de threads (par défaut on prend le nombre de coeurs du CPU) :

`cargo build --jobs {{nombre_de_threads}}`
