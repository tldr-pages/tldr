# cargo clean

> Rimuovi gli artefatti generati nella directory `target`.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-clean.html>.

- Rimuovi l'intera directory `target`:

`cargo clean`

- Rimuovi gli artefatti della documentazione (la directory `target/doc`):

`cargo clean --doc`

- Rimuovi gli artefatti di release (la directory `target/release`):

`cargo clean {{[-r|--release]}}`

- Rimuovi gli artefatti nella directory del profilo specificato (in questo caso `target/debug`):

`cargo clean --profile {{dev}}`
