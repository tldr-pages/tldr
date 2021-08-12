# cargo build

> Compilați un pachet local și toate dependențele acestuia.
> Mai multe informaţii: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>

- Construiți pachetul sau pachetele definite de fișierul manifest `Cargo.toml` în calea locală:

`cargo build`

- Construiți artefacte în modul de eliberare, cu optimizări:

`cargo build --release`

- Necesită ca `Cargo.lock` să fie la zi:

`cargo build --locked`

- Construiți toate pachetele în spațiul de lucru:

`cargo build --workspace`

- Construiți un pachet specific:

`cargo build --package {{package}}`

- Construiți numai binarul specificat:

`cargo build --bin {{name}}`

- Construiți numai ținta de testare specificată:

`cargo build --test {{testname}}`
