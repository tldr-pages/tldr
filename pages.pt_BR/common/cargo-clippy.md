# cargo clippy

> Conjunto de validadores para identificar erros comuns e melhorar código em Rust.
> Mais informações: <https://github.com/rust-lang/rust-clippy>.

- Executa verificações no código no diretório atual:

`cargo clippy`

- Executa verificações garantindo que o `Cargo.lock` esteja atualizado:

`cargo clippy --locked`

- Executa verificações em todos os pacotes no workspace:

`cargo clippy --workspace`

- Executa verificações para um pacote específico:

`cargo clippy --package {{pacote}}`

- Executa validações tratando avisos como erros:

`cargo clippy -- --deny warnings`

- Executa verificações e ignora avisos:

`cargo clippy -- --allow warnings`

- Aplica automaticamente as sugestões do Clippy:

`cargo clippy --fix`
