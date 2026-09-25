# cargo report

> Mostra vari tipi di report.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-report.html>.

- Mostra un report dei crate che smetteranno di compilare in futuro:

`cargo report future-incompatibilities`

- Mostra un report con l'ID generato da Cargo specificato:

`cargo report future-incompatibilities --id {{id}}`

- Mostra un report per il pacchetto specificato:

`cargo report future-incompatibilities {{[-p|--package]}} {{pacchetto}}`
