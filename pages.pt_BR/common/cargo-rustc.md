# cargo rustc

> Compila um pacote Rust.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- Compilar o pacote ou pacotes definidos pelo arquivo `Cargo.toml` no diretório de trabalho atual:

`cargo rustc`

- Compilar os artefatos em modo de publicação (release), com otimizações:

`cargo rustc --release`

- Compilar com otimizações específicas para a arquitetura do CPU atual:

`cargo rustc --release -- -C target-cpu=native`

- Compilar com otimização de velocidade:

`cargo rustc -- -C opt-level {{1|2|3}}`

- Compilar com otimização de tamanho (`z` também desativa a vetorização de ciclos):

`cargo rustc -- -C opt-level {{s|z}}`

- Verificar se o pacote usa código com padrões inseguros de acesso à memória:

`cargo rustc --lib -- -D unsafe-code`

- Compilar um pacote específico:

`cargo rustc --package {{pacote}}`

- Compilar apenas o binário especificado:

`cargo --bin {{nome}}`
