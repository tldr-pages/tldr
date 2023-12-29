# cargo build

> Compila um projeto Rust em um pacote local incluindo todas as suas dependências.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Compila o pacote ou pacotes definidos pelo arquivo `Cargo.toml` no diretório local:

`cargo build`

- Compila os artefatos em modo de publicação (release), com otimizações:

`cargo build --release`

- Compila um pacote garantindo que o `Cargo.lock` esteja atualizado:

`cargo build --locked`

- Compila todos os pacotes no workspace:

`cargo build --workspace`

- Compila um pacote específico:

`cargo build --package {{pacote}}`

- Compila apenas o binário especificado:

`cargo build --bin {{nome}}`

- Compila apenas um teste específico:

`cargo build --test {{nome_do_teste}}`
