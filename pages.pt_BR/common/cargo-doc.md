# cargo doc

> Constrói e visualiza a documentação de um pacote Rust, opcionalmente em modo offline.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Construir a documentação padrão do pacote e mostrá-la no navegador:

`cargo doc --open`

- Construir a documentação sem acessar a rede:

`cargo doc --offline`

- Visualizar a documentação de um pacote específico:

`cargo doc --open --package {{pacote}}`

- Visualizar a documentação de um pacote específico sem acessar a rede:

`cargo doc --open --offline --package {{pacote}}`
