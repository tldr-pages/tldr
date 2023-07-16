# cargo doc

> Construir e visualizar a documentação de um pacote Rust offline.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Construir e visualizar a documentação padrão do pacote no navegador:

`cargo doc --open`

- Construir a documentação sem acessar a rede:

`cargo doc --offline`

- Visualizar a documentação de um pacote específico:

`cargo doc --open --package {{pacote}}`

- Visualizar a documentação de um pacote específico offline:

`cargo doc --open --offline --package {{pacote}}`
