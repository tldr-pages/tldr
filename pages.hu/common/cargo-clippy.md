# cargo clippy

> Linták gyűjteménye a gyakori hibák kiszűrésére és a Rust kód javítására. További információ: <https://github.com/rust-lang/rust-clippy>.

- Ellenőrzéseket futtat az aktuális könyvtárban lévő kódon:

`cargo clippy`

- Követelmény, hogy a `Cargo.lock` naprakész legyen:

`cargo clippy --locked`

- Ellenőrzések futtatása a munkaterület összes csomagján:

`cargo clippy --workspace`

- Ellenőrzések futtatása egy csomagra vonatkozóan:

`cargo clippy --package {{package}}`

- A figyelmeztetéseket hibaként kezelje:

`cargo clippy -- --deny warnings`

- Ellenőrzések futtatása és a figyelmeztetések figyelmen kívül hagyása:

`cargo clippy -- --allow warnings`

- Clippy javaslatok automatikus alkalmazása:

`cargo clippy --fix`
