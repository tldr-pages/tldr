# cargo bench

> Compila ed esegui i benchmark.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-bench.html>.

- Esegui tutti i benchmark di un pacchetto:

`cargo bench`

- Non interrompere quando un benchmark fallisce:

`cargo bench --no-fail-fast`

- Compila, ma non eseguire i benchmark:

`cargo bench --no-run`

- Esegui il benchmark specificato:

`cargo bench --bench {{benchmark}}`

- Esegui il benchmark con il profilo specificato (predefinito: `bench`):

`cargo bench --profile {{profilo}}`

- Esegui il benchmark di tutti i target example:

`cargo bench --examples`

- Esegui il benchmark di tutti i target binari:

`cargo bench --bins`

- Esegui il benchmark della libreria del pacchetto:

`cargo bench --lib`
