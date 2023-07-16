# cargo build

> Compilar um pacote local e todas as suas dependências.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Compilar o pacote ou pacotes definidos pelo arquivo `Cargo.toml` no diretório local:

`cargo build`

- Compilar os artefatos em modo de lançamento (release), com otimizações:

`cargo build --release`

- Exigir que o `Cargo.lock` esteja atualizado:

`cargo build --locked`

- Compilar todos os pacotes no workspace:

`cargo build --workspace`

- Compilar um pacote específico:

`cargo build --package {{pacote}}`

- Compilar apenas o binário especificado:

`cargo build --bin {{nome}}`

- Compilar apenas o teste específico:

`cargo build --test {{nome_do_teste}}`
