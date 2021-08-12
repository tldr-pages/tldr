# cargo rustc

> Compilați un pachet Rust și transmiteți opțiuni suplimentare compilatorului.
> Mai multe informaţii: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>

- Construiți pachetul sau pachetele definite de fișierul manifest `Cargo.toml` în directorul curent de lucru:

`cargo rustc`

- Construiți artefacte în modul de eliberare, cu optimizări:

`cargo rustc --release`

- Compilați cu optimizări specifice arhitecturii pentru CPU curent:

`cargo rustc --release -- -C target-cpu=native`

- Compilați cu optimizarea vitezei:

`cargo rustc -- -C opt-level {{1|2|3}}`

- Compilare cu [s] ize optimizare (`z`, de asemenea, dezactivează vectorizarea buclei):

`cargo rustc -- -C opt-level {{s|z}}`

- Verificați dacă pachetul dvs. utilizează cod nesigur:

`cargo rustc --lib -- -D unsafe-code`

- Construiți un pachet specific:

`cargo rustc --package {{package}}`

- Construiți numai binarul specificat:

`cargo --bin {{name}}`
