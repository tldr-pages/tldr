# cargo test

> Egy Rust csomag egység- és integrációs tesztjeinek végrehajtása. További információ: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- Csak olyan tesztek futtatása, amelyek egy adott karakterláncot tartalmaznak a nevükben:

`cargo test {{testname}}`

- Az egyidejűleg futó tesztesetek számának beállítása:

`cargo test -- --test-threads={{count}}`

- A `Cargo.lock` naprakészségének megkövetelése:

`cargo test --locked`

- Az artefaktumok tesztelése kiadási módban, optimalizációkkal:

`cargo test --release`

- A munkaterület összes csomagjának tesztelése:

`cargo test --workspace`

- Egy csomag tesztjeinek futtatása:

`cargo test --package {{package}}`

- Tesztek futtatása a tesztvégrehajtások kimeneteinek elrejtése nélkül:

`cargo test -- --nocapture`
