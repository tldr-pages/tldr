# cargo add

> Adiciona dependências ao arquivo `Cargo.toml` de um projeto Rust.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- Adiciona a versão mais recente de uma dependência ao projeto atual:

`cargo add {{dependência}}`

- Adiciona uma versão específica de uma dependência:

`cargo add {{dependência}}@{{versão}}`

- Adiciona uma dependência e habilita uma ou mais funcionalidades específicas:

`cargo add {{dependência}} --features {{funcionalidade_1}},{{funcionalidade_2}}`

- Adiciona uma dependência opcional, que será exposta como uma funcionalidade da crate:

`cargo add {{dependência}} --optional`

- Adiciona uma crate local como dependência:

`cargo add --path {{caminho/para/crate}}`

- Adiciona uma dependência de desenvolvimento ou de compilação:

`cargo add {{dependência}} --{{dev|build}}`

- Adiciona uma dependência com todas as funcionalidades padrão desabilitadas:

`cargo add {{dependência}} --no-default-features`
