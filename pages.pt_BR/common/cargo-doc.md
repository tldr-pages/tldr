# cargo doc

> Constrói e visualiza a documentação de um pacote Rust, opcionalmente em modo offline.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Constrói a documentação padrão do pacote e mostrá-la no navegador:

`cargo doc --open`

- Não constrói documentação de dependências:

`cargo doc --no-deps`

- Constrói e visualiza a documentação em um navegador:

`cargo doc --open --package`

- Constrói e visualiza a documentação de um pacote específico:

`cargo doc --open --package {{pacote}}`
