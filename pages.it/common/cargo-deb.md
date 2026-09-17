# cargo deb

> Crea pacchetti Debian da progetti Cargo.
> Nota: questo non è un comando integrato di Cargo; va installato separatamente.
> Maggiori informazioni: <https://github.com/kornelski/cargo-deb>.

- Crea un pacchetto Debian da un progetto:

`cargo deb`

- Scrivi il file `.deb` nella directory o file specificato:

`cargo deb {{[-o|--output]}} {{path/to/file_or_directory}}`

- Compila per il target Rust specificato:

`cargo deb --target {{x86_64-unknown-linux-gnu}}`

- Seleziona quale pacchetto usare in un workspace Cargo:

`cargo deb {{[-p|--package]}} {{package_name}}`

- Installa immediatamente il pacchetto creato:

`cargo deb --install`
