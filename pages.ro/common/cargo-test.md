# cargo test

> Executați testele de unitate și integrare ale unui pachet Rust.
> Mai multe informaţii: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>

- Executați numai teste care conțin un anumit șir în numele lor:

`cargo test {{testname}}`

- Setați numărul de cazuri de testare simultane:

`cargo test -- --test-threads={{count}}`

- Necesită ca `Cargo.lock` să fie la zi:

`cargo test --locked`

- Test artefacte în modul de eliberare, cu optimizări:

`cargo test --release`

- Testați toate pachetele din spațiul de lucru:

`cargo test --workspace`

- Executați teste pentru un pachet:

`cargo test --package {{package}}`
