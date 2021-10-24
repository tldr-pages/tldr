# rvm

> Ferramenta que facilita a instalação e gerenciamento de múltiplas versões da linguagem Ruby.
> Mais informações: <https://rvm.io>.

- Instalar uma ou mais versões separadas por espaço:

`rvm install {{uma_ou_mais_versoes}}`

- Exibir a lista de versões instaladas:

`rvm list`

- Definir uma versão específica para ser utilizada temporariamente:

`rvm use {{versao}}`

- Definir uma versão específica para ser a instalação padrão:

`rvm --default use {{versao}}`

- Atualizar uma versão já instalada para uma nova versão:

`rvm upgrade {{versao_atual}} {{nova_versao}}`

- Remover uma versão mantendo o código fonte:

`rvm uninstall {{versao}}`

- Remover uma versão e o código fonte:

`rvm remove {{versao}}`

- Exibir as dependências específicas para o seu sistema operacional:

`rvm requirements`
