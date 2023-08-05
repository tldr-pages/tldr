# cargo test

> Executa os testes unitários e de integração de um pacote Rust.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- Executar apenas os testes que contenham uma string específica em seus nomes:

`cargo test {{nomedoteste}}`

- Definir o número de casos de teste para execução simultânea:

`cargo test -- --test-threads={{quantidade}}`

- Executar os testes garantindo que o `Cargo.lock` esteja atualizado:

`cargo test --locked`

- Testar os artefatos em modo de publicação (release), com otimizações:

`cargo test --release`

- Testar todos os pacotes no workspace:

`cargo test --workspace`

- Executar testes para um pacote específico:

`cargo test --package {{pacote}}`

- Executar testes sem ocultar a saída das execuções dos testes:

`cargo test -- --nocapture`
