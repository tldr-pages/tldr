# cargo bench
> Compila ed esegue i benchmark.
> More information: <https://doc.rust-lang.org/cargo/commands/cargo-bench.html>.

- Esegue tutti i benchmark di un package:
`cargo bench`

- Non interrompe l'esecuzione quando un benchmark fallisce:
`cargo bench --no-fail-fast`

- Compila, ma non esegue i benchmark:
`cargo bench --no-run`

- Esegue il benchmark specificato:
`cargo bench --bench {{benchmark}}`

- Esegue il benchmark con il profilo indicato (predefinito: `bench`):
`cargo bench --profile {{profilo}}`

- Esegue tutti i target di esempio:
`cargo bench --examples`

- Esegue tutti i target binari:
`cargo bench --bins`

- Esegue il benchmark della libreria del package:
`cargo bench --lib`