# cargo test

> Esegui i test unitari e di integrazione di un pacchetto Rust.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- Esegui solo i test che contengono una stringa specifica nel loro nome:

`cargo {{[t|test]}} {{test_name}}`

- Imposta il numero di casi di test eseguiti contemporaneamente:

`cargo {{[t|test]}} -- --test-threads {{count}}`

- Esegui i test in modalità release, con ottimizzazioni:

`cargo {{[t|test]}} {{[-r|--release]}}`

- Esegui i test per tutti i pacchetti nello workspace:

`cargo {{[t|test]}} --workspace`

- Esegui i test per un pacchetto specifico:

`cargo {{[t|test]}} {{[-p|--package]}} {{package}}`

- Esegui i test senza nascondere l'output delle esecuzioni dei test:

`cargo {{[t|test]}} -- --nocapture`
