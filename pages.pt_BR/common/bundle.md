# bundle

> Gerenciador de dependências da linguagem de programação Ruby.
> Mais informações: <https://bundler.io/man/bundle.1.html>.

- Instalar todas as gemas definidas no `Gemfile`:

`bundle install`

- Atualizar todas as gemas, respeitando as regras definidas no `Gemfile`, e recriar o arquivo `Gemfile.lock`:

`bundle update`

- Atualizar uma gema específica definida no `Gemfile`:

`bundle update --source {{nome_da_gema}}`

- Criar o esqueleto do projeto de uma nova gema:

`bundle gem {{nome_da_gema}}`
