# cargo add

> Függőségek hozzáadása egy Rust projekt `Cargo.toml` fájljához. További információ: <https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- Egy függőség legújabb verziójának hozzáadása az aktuális projekthez:

`cargo add {{dependency}}`

- Egy függőség adott verziójának hozzáadása:

`cargo add {{dependency}}@{{version}}`

- Függőség hozzáadása és egy vagy több konkrét funkció engedélyezése:

`cargo add {{dependency}} --features {{feature_1}},{{feature_2}}`

- Hozzáad egy opcionális függőséget, amely aztán a crate egyik funkciójaként lesz láthatóvá:

`cargo add {{dependency}} --optional`

- Helyi crate hozzáadása függőségként:

`cargo add --path {{path/to/crate}}`

- Fejlesztési vagy építési függőség hozzáadása:

`cargo add {{dependency}} --{{dev|build}}`

- Függőség hozzáadása az összes alapértelmezett funkció letiltásával:

`cargo add {{dependency}} --no-default-features`
