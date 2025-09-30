# cargo test

> Executa os testes unitários e de integração de um pacote Rust.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- Executa apenas os testes que contenham um texto específico em seus nomes:

`cargo {{[t|test]}} {{nomedoteste}}`

- Define o número de casos de teste para execução simultânea:

`cargo {{[t|test]}} -- --test-threads {{quantidade}}`

- Testa os artefatos em modo de publicação (release), com otimizações:

`cargo {{[t|test]}} {{[-r|--release]}}`

- Testa todos os pacotes no workspace:

`cargo {{[t|test]}} --workspace`

- Executa testes para um pacote específico:

`cargo {{[t|test]}} {{[-p|--package]}} {{pacote}}`

- Executa testes sem ocultar a saída das execuções dos testes:

`cargo {{[t|test]}} -- --nocapture`
