# cargo package

> Assembla un pacchetto locale in un tarball distribuibile (un file `.crate`).
> Simile a `cargo publish --dry-run`, ma offre più opzioni.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-package.html>.

- Esegui i controlli e crea un file `.crate` (equivalente a `cargo publish --dry-run`):

`cargo package`

- Mostra quali file sarebbero inclusi nel tarball senza crearli effettivamente:

`cargo package {{[-l|--list]}}`
