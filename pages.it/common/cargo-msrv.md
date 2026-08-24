# cargo msrv

> Gestisci la Minimum Supported Rust Version (MSRV) di un progetto.
> Nota: questo non è un comando integrato di Cargo; va installato separatamente.
> Maggiori informazioni: <https://gribnau.dev/cargo-msrv/>.

- Mostra le MSRV delle dipendenze (come specificato nei loro `Cargo.toml`):

`cargo msrv list`

- Trova la MSRV del progetto provando a compilarlo con toolchain differenti:

`cargo msrv find`

- Mostra la MSRV del progetto come specificata in `Cargo.toml`:

`cargo msrv show`

- Imposta la MSRV in `Cargo.toml` a una versione di Rust data:

`cargo msrv set {{versione}}`

- Verifica se la MSRV è soddisfacibile compilando il progetto con la versione specificata di Rust:

`cargo msrv verify`
