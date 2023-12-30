# cargo rustc

> Compila um pacote Rust.
> Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- Compila o pacote e passa opções para `rustc`:

`cargo rustc -- {{rustc_options}}`

- Compila os artefatos em modo de publicação (release), com otimizações:

`cargo rustc --release`

- Compila com otimizações específicas para a arquitetura do CPU atual:

`cargo rustc --release -- -C target-cpu=native`

- Compila com otimização de velocidade:

`cargo rustc -- -C opt-level {{1|2|3}}`

- Compila com otimização de tamanho (`z` também desativa a vetorização de ciclos):

`cargo rustc -- -C opt-level {{s|z}}`

- Verifica se o pacote usa código com padrões inseguros de acesso à memória:

`cargo rustc --lib -- -D unsafe-code`

- Compila um pacote específico:

`cargo rustc --package {{pacote}}`

- Compila apenas o binário especificado:

`cargo --bin {{nome}}`
