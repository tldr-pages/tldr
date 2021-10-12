# rustc

> O compilador Rust.
> Processa, compila e vincula arquivos fonte da linguagem Rust.
> Mais informações: <https://doc.rust-lang.org/rustc>.

- Compila um único arquivo:

`rustc {{arquivo.rs}}`

- Compila com alta otimização:

`rustc -O {{arquivo.rs}}`

- Compila com informações de depuração:

`rustc -g {{arquivo.rs}}`

- Compila com otimizações específicas de arquitetura para a CPU atual:

`rustc -C target-cpu=native {{caminho/para/arquivo.rs}}`

- Exibe otimizações específicas de arquitetura para a CPU atual:

`rustc -C target-cpu=native --print cfg`

- Exibe lista de targets:

`rustc --print target-list`

- Compila para um target específico:

`rustc --target {{target_triplo}} {{caminho/para/arquivo.rs}}`
