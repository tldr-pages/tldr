# cargo clippy

> Um conjunto de lints para identificar erros comuns e melhorar o seu código Rust.
> Mais informações: <https://github.com/rust-lang/rust-clippy>.

- Executar verificações no código no diretório atual:

`cargo clippy`

- Exigir que o `Cargo.lock` esteja atualizado:

`cargo clippy --locked`

- Executar verificações em todos os pacotes no workspace:

`cargo clippy --workspace`

- Executar verificações para um pacote específico:

`cargo clippy --package {{pacote}}`

- Tratar avisos como erros:

`cargo clippy -- --deny warnings`

- Executar verificações e ignorar avisos:

`cargo clippy -- --allow warnings`

- Aplicar automaticamente as sugestões do Clippy:

`cargo clippy --fix`
