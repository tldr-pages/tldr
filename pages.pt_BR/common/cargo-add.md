# cargo add

> Adiciona dependências ao arquivo `Cargo.toml` de um projeto Rust.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- Adicionar a versão mais recente de uma dependência ao projeto atual:

`cargo add {{dependência}}`

- Adicionar uma versão específica de uma dependência:

`cargo add {{dependência}}@{{versão}}`

- Adicionar uma dependência e habilitar uma ou mais funcionalidades específicas:

`cargo add {{dependência}} --features {{funcionalidade_1}},{{funcionalidade_2}}`

- Adicionar uma dependência opcional, que será exposta como uma funcionalidade da crate:

`cargo add {{dependência}} --optional`

- Adicionar uma crate local como dependência:

`cargo add --path {{caminho/para/crate}}`

- Adicionar uma dependência de desenvolvimento ou de compilação:

`cargo add {{dependência}} --{{dev|build}}`

- Adicionar uma dependência com todas as funcionalidades padrão desabilitadas:

`cargo add {{dependência}} --no-default-features`
