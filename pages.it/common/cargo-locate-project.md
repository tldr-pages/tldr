# cargo locate-project

> Stampa il percorso completo al manifesto `Cargo.toml` di un progetto.
> Se il progetto fa parte di uno workspace, viene mostrato il manifesto del progetto e non quello dello workspace.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-locate-project.html>.

- Visualizza l'oggetto JSON con il percorso completo al manifesto `Cargo.toml`:

`cargo locate-project`

- Visualizza il percorso del progetto nel formato specificato:

`cargo locate-project --message-format {{plain|json}}`

- Visualizza il manifesto `Cargo.toml` situato alla radice dello workspace anziché del membro corrente:

`cargo locate-project --workspace`

- Visualizza il manifesto `Cargo.toml` di una directory specificata:

`cargo locate-project --manifest-path {{percorso/del/Cargo.toml}}`
