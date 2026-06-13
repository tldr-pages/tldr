# cargo fmt

> Esegui `rustfmt` su tutti i file sorgente di un progetto Rust.
> Vedi anche: `rustfmt`.
> Maggiori informazioni: <https://github.com/rust-lang/rustfmt>.

- Formatta tutti i file sorgente:

`cargo fmt`

- Controlla la presenza di errori di formattazione senza modificare i file:

`cargo fmt --check`

- Passa argomenti a ogni chiamata di `rustfmt`:

`cargo fmt -- {{rustfmt_args}}`
