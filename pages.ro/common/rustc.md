# rustc

> Compilatorul Rust.
> Procesează, compilează și leagă fișierele sursă de limbă rugină.
> Mai multe informaţii: <https://doc.rust-lang.org/rustc>

- Compilarea unui singur fișier:

`rustc {{file.rs}}`

- Compilați cu optimizare ridicată:

`rustc -O {{file.rs}}`

- Compilați cu informații de depanare:

`rustc -g {{file.rs}}`

- Compilați cu optimizări specifice arhitecturii pentru CPU curent:

`rustc -C target-cpu=native {{path/to/file.rs}}`

- Afișează optimizări specifice arhitecturii pentru procesorul curent:

`rustc -C target-cpu=native --print cfg`

- Afișează lista țintă:

`rustc --print target-list`

- Compilați pentru o anumită țintă:

`rustc --target {{target_triple}} {{path/to/file.rs}}`
