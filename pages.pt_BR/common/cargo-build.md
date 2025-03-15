# cargo build

> Compila um projeto Rust em um pacote local incluindo todas as suas dependências.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Compila o pacote ou pacotes definidos pelo arquivo `Cargo.toml` no diretório local:

`cargo {{[b|build]}}`

- Compila os artefatos em modo de publicação (release), com otimizações:

`cargo {{[b|build]}} {{[-r|--release]}}`

- Compila um pacote garantindo que o `Cargo.lock` esteja atualizado:

`cargo {{[b|build]}} --locked`

- Compila todos os pacotes no workspace:

`cargo {{[b|build]}} --workspace`

- Compila um pacote específico:

`cargo {{[b|build]}} {{[-p|--package]}} {{pacote}}`

- Compila apenas o binário especificado:

`cargo {{[b|build]}} --bin {{nome}}`

- Compila apenas um teste específico:

`cargo {{[b|build]}} --test {{nome_do_teste}}`
