# cargo init

> Crea un nuovo pacchetto Cargo.
> Equivalente a `cargo new`, ma specificare una directory è opzionale.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-init.html>.

- Inizializza un progetto Rust con target binario nella directory corrente:

`cargo init`

- Inizializza un progetto Rust con target binario nella directory specificata:

`cargo init {{percorso/della/directory}}`

- Inizializza un progetto Rust con target libreria nella directory corrente:

`cargo init --lib`

- Inizializza un repository di controllo versione nella directory del progetto (predefinito: `git`):

`cargo init --vcs {{git|hg|pijul|fossil|none}}`

- Imposta il nome del pacchetto (predefinito: nome della directory):

`cargo init --name {{nome}}`
