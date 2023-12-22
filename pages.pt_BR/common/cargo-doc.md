# cargo doc

> Constrói e visualiza a documentação de um pacote Rust, opcionalmente em modo offline.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Constrói a documentação padrão do pacote e mostrá-la no navegador:

`cargo doc --open`

- Constrói a documentação sem acessar a rede:

`cargo doc --offline`

- Visualiza a documentação de um pacote específico:

`cargo doc --open --package {{pacote}}`

- Visualiza a documentação de um pacote específico sem acessar a rede:

`cargo doc --open --offline --package {{pacote}}`
