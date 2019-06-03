# cargo

> Gestore di pacchetti di Rust.
> Gestisce progetti Rust ed i moduli dai quali sono dipendenti (detti crate).
> Maggiori informazioni: <https://crates.io/>.

- Cerca una crate:

`cargo search {{termine_di_ricerca}}`

- Installa una crate:

`cargo install {{nome_crate}}`

- Elenca crate installate:

`cargo install --list`

- Crea un nuovo progetto Rust binario o di libreria nella directory corrente:

`cargo init --{{bin|lib}}`

- Crea un nuovo progetto Rust binario o di libreria nella directory specificata:

`cargo new {{path/a/directory}} --{{bin|lib}}`

- Builda il progetto Rust nella cartella corrente:

`cargo build`

- Builda utilizzando più job (thread) paralleli:

`cargo build -j {{numero_job}}`
