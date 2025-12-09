# cargo run

> Voer het huidige Cargo-pakket uit.
> Opmerking: de werkmap van de uitgevoerde binary wordt ingesteld op de huidige werkmap.
> Meer informatie: <https://doc.rust-lang.org/cargo/commands/cargo-run.html>.

- Voer de standaard binary uit:

`cargo {{[r|run]}}`

- Voer de opgegeven binary uit:

`cargo {{[r|run]}} --bin {{naam}}`

- Voer het opgegeven voorbeeld uit:

`cargo {{[r|run]}} --example {{naam}}`

- Activeer een door spaties of komma's gescheiden lijst met features:

`cargo {{[r|run]}} {{[-F|--features]}} "{{feature1 feature2 ...}}"`

- Schakel de standaardfeatures uit:

`cargo {{[r|run]}} --no-default-features`

- Activeer alle beschikbare features:

`cargo {{[r|run]}} --all-features`

- Voer uit met het opgegeven profiel:

`cargo {{[r|run]}} --profile {{naam}}`
