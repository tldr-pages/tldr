# cargo check
> Controlla un package locale e tutte le sue dipendenze per individuare errori.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-check.html>.

- Controlla il package corrente:
`cargo {{[c|check]}}`

- Controlla tutti i test:
`cargo {{[c|check]}} --tests`

- Controlla i test di integrazione in `tests/integration_test1.rs`:
`cargo {{[c|check]}} --test {{integration_test1}}`

- Controlla il package corrente con le feature `feature1` e `feature2`:
`cargo {{[c|check]}} {{[-F|--features]}} {{feature1,feature2}}`

- Controlla il package corrente con le feature predefinite disabilitate:
`cargo {{[c|check]}} --no-default-features`