# cargo check

> Controlla un pacchetto locale e tutte le sue dipendenze alla ricerca di errori.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-check.html>.

- Controlla il pacchetto corrente:

`cargo {{[c|check]}}`

- Controlla tutti i test:

`cargo {{[c|check]}} --tests`

- Controlla l'integration test `tests/integration_test1.rs`:

`cargo {{[c|check]}} --test {{integration_test1}}`

- Controlla il pacchetto corrente con le feature `feature1` e `feature2`:

`cargo {{[c|check]}} {{[-F|--features]}} {{feature1,feature2}}`

- Controlla il pacchetto corrente con le feature di default disabilitate:

`cargo {{[c|check]}} --no-default-features`
