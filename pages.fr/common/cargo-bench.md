# cargo bench

> Compile et exécute des benchmarks.
> Plus d'informations : <https://doc.rust-lang.org/cargo/commands/cargo-bench.html>.

- Exécute tous les benchmarks d'un paquet :

`cargo bench`

- Ne pas arréter quand un benchmark échoue :

`cargo bench --no-fail-fast`

- Compile, mais n'exécute pas les benchmarks :

`cargo bench --no-run`

- Exécute le benchmark spécifié :

`cargo bench --bench {{benchmark}}`

- Exécute les benchmarks avec un profile spécifique (défaut : `bench`) :

`cargo bench --profile {{profile}}`

- Exécute les benchmarks sur tous les exemples cibles :

`cargo bench --examples`

- Exécute les benchmarks sur tous les binaires cibles :

`cargo bench --bins`

- Exécute les benchmarks sur la bibliothèque du paquet :

`cargo bench --lib`
