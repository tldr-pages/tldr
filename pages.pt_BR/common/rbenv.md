# rbenv

> Ferramenta que facilita a instalação e gerenciamento de múltiplas versões da linguagem Ruby.
> Mais informações: <https://github.com/rbenv/rbenv>.

- Instalar uma ou mais versões, separadas por espaço:

`rbenv install {{uma_ou_mais_versoes}}`

- Exibir a lista de versões instaladas:

`rbenv versions`

- Determinar uma versão específica para ser a instalação padrão:

`rbenv global {{versao}}`

- Determinar uma versão específica para um projeto. Este comando deve ser executado no diretório do projeto:

`rbenv local {{versao}}`

- Exibir a versão ativa:

`rbenv version`

- Remover uma versão:

`rbenv uninstall {{versao}}`

- Exibir todas as versões que contém um determinado executável:

`rbenv whence {{executavel}}`
