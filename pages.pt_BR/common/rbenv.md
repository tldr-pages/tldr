# rbenv

> Ferramenta que facilita a instalação e gerenciamento de múltiplas versões da linguagem Ruby.
> Mais informações: <https://github.com/rbenv/rbenv>.

- Instala uma ou mais versões, separadas por espaço:

`rbenv install {{uma_ou_mais_versoes}}`

- Exibe a lista de versões instaladas:

`rbenv versions`

- Determina uma versão específica para ser a instalação padrão:

`rbenv global {{versao}}`

- Determina uma versão específica para um projeto. Este comando deve ser executado no diretório do projeto:

`rbenv local {{versao}}`

- Exibe a versão ativa:

`rbenv version`

- Remove uma versão:

`rbenv uninstall {{versao}}`

- Exibe todas as versões que contém um determinado executável:

`rbenv whence {{executavel}}`
