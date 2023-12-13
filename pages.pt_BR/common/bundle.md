# bundle

> Gerenciador de dependências da linguagem de programação Ruby.
> Mais informações: <https://bundler.io/man/bundle.1.html>.

- Instalar todas as gemas definidas no `Gemfile` esperadas no diretório de trabalho:

`bundle install`

- Executar um comando no contexto do pacote atual:

`bundle exec {{comando}} {{argumentos}}`

- Atualizar todas as gemas respeitando as regras definidas no `Gemfile` e recriar o arquivo `Gemfile.lock`:

`bundle update`

- Atualizar uma ou mais gema(s) específicas definidas no `Gemfile`:

`bundle update {{nome_da_gema1}} {{nome_da_gema2}}`

- Atualizar uma ou mais gema(s) específicas definidas no `Gemfile` mas somente para a próxima versão de patch:

`bundle update --patch {{nome_da_gema1}} {{nome_da_gema2}}`

- Atualizar todas as gemas do grupo especificado no `Gemfile`:

`bundle update --group {{desenvolvimento}}`

- Listar gemas instaladas no `Gemfile` com novas versões disponíveis:

`bundle outdated`

- Criar o esqueleto do projeto de uma nova gema:

`bundle gem {{nome_da_gema}}`
