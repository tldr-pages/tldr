# rustfmt

> Instrument pentru formatarea codului sursă Rust.
> Mai multe informaţii: <https://github.com/rust-lang/rustfmt>

- Formatarea unui fișier, suprascrierea fișierului original în loc:

`rustfmt {{source.rs}}`

- Verificați un fișier pentru formatare și afișați orice modificări pe consola:

`rustfmt --check {{source.rs}}`

- Copierea de rezervă a fișierelor modificate înainte de formatare (fișierul original este redenumit cu o extensie `.bk`):

`rustfmt --backup {{source.rs}}`
