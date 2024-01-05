# rustc

> O compilador Rust.
> Projetos Rust geralmente usam o `cargo` em vez de chamar `rustc` diretamente.
> Mais informações: <https://doc.rust-lang.org/rustc>.

- Compila uma crate binária:

`rustc {{caminho/para/arquivo.rs}}`

- Compila com otimizações (s significa otimizar o tamanho do binário; z é o mesmo com ainda mais otimizações):

`rustc -C lto -C opt-level={{0|1|2|3|s|z}} {{caminho/para/arquivo.rs}}`

- Compila com informações de depuração:

`rustc -g {{caminho/para/arquivo.rs}}`

- Explica uma mensagem de erro:

`rustc --explain {{código_de_erro}}`

- Compila com otimizações específicas de arquitetura para a CPU atual:

`rustc -C target-cpu={{native}} {{caminho/para/arquivo.rs}}`

- Exibe lista de targets:

`rustc --print target-list`

- Compila para um target específico:

`rustc --target {{target_triplo}} {{caminho/para/arquivo.rs}}`
