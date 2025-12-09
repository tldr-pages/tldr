# cargo doc

> Constrói e visualiza a documentação de um pacote Rust, opcionalmente em modo offline.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Constrói a documentação do projeto atual e de todas as dependências:

`cargo {{[d|doc]}}`

- Não constrói documentação de dependências:

`cargo {{[d|doc]}} --no-deps`

- Constrói e visualiza a documentação em um navegador:

`cargo {{[d|doc]}} --open`

- Constrói e visualiza a documentação de um pacote específico:

`cargo {{[d|doc]}} --open {{[-p|--package]}} {{pacote}}`
