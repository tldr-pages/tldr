# cargo doc

> Constrói e visualiza a documentação de um pacote Rust, opcionalmente em modo offline.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Constrói a documentação do projeto atual e de todas as dependências:

`cargo doc`

- Não constrói documentação de dependências:

`cargo doc --no-deps`

- Constrói e visualiza a documentação em um navegador:

`cargo doc --open`

- Constrói e visualiza a documentação de um pacote específico:

`cargo doc --open --package {{pacote}}`
