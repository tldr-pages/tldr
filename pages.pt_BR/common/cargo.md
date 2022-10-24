# cargo

> Gerencia projetos Rust e as dependências dos modulos (crates).
> Alguns subcomandos como `cargo build` tem a sua própria documentação.
> Mais informações: <https://crates.io>.

- Procura por crates:

`cargo search {{string_procurada}}`

- Instala uma crate:

`cargo install {{nome_da_crate}}`

- Lista as crates instaladas:

`cargo install --list`

- Cria um projeto Rust sendo binário ou uma biblioteca no diretório atual:

`cargo init --{{bin|lib}}`

- Cria um projeto Rust sendo binário ou uma biblioteca em um diretório específico:

`cargo new {{caminho/para/directório}} --{{bin|lib}}`

- Constrói o projeto Rust no diretório atual:

`cargo build`

- Constrói o projeto Rust no diretório atual utilizando o nightly compilador:

`cargo +nightly build`

- Constrói o projeto Rust utilizando um número específico de threads (padrão é o número de cores do CPU):

`cargo build --jobs {{número_de_threads}}`
