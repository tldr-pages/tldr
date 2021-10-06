# rustc

> O compilador Rust.
> Processa, compila e vincula arquivos fonte da linguagem Rust.
> Mais informações: <https://doc.rust-lang.org/rustc>.

- Compilar um único arquivo:

`rustc {{arquivo.rs}}`

- Compilar com alta otimização:

`rustc -O {{arquivo.rs}}`

- Compilar com informações de depuração:

`rustc -g {{arquivo.rs}}`

- Compilar com otimizações específicas de arquitetura para a CPU atual:

`rustc -C target-cpu=native {{caminho/para/arquivo.rs}}`

- Exibir otimizações específicas de arquitetura para a CPU atual:

`rustc -C target-cpu=native --print cfg`

- Exibir lista de targets:

`rustc --print target-list`

- Compilar para um target específico:

`rustc --target {{target_triplo}} {{caminho/para/arquivo.rs}}`
