# cargo

> Gestisce progetti Rust e le loro dipendenze (crate).
> Alcuni sottocomandi come `build` hanno la propria documentazione.
> Maggiori informazioni: <https://doc.rust-lang.org/stable/cargo/>.

- Cerca crate:

`cargo search {{stringa_di_ricerca}}`

- Installa un crate binario:

`cargo install {{nome_crate}}`

- Elenca i crate binari installati:

`cargo install --list`

- Crea un nuovo progetto Rust binario o libreria nella directory specificata:

`cargo init --{{bin|lib}} {{percorso/della/directory}}`

- Aggiungi una dipendenza a `Cargo.toml` nella directory corrente:

`cargo add {{dipendenza}}`

- Compila il progetto Rust con il profilo release:

`cargo {{[b|build]}} {{[-r|--release]}}`

- Compila il progetto con il compilatore nightly (richiede `rustup`):

`cargo +nightly {{[b|build]}}`

- Compila usando un numero specifico di thread:

`cargo {{[b|build]}} {{[-j|--jobs]}} {{numero_thread}}`
