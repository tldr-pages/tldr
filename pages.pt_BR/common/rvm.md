# rvm

> Ferramenta que facilita a instalação e gerenciamento de múltiplas versões da linguagem Ruby.
> Mais informações: <https://rvm.io>.

- Instala uma ou mais versões separadas por espaço:

`rvm install {{uma_ou_mais_versoes}}`

- Exibe a lista de versões instaladas:

`rvm list`

- Define uma versão específica para ser utilizada temporariamente:

`rvm use {{versao}}`

- Define uma versão específica para ser a instalação padrão:

`rvm --default use {{versao}}`

- Atualiza uma versão já instalada para uma nova versão:

`rvm upgrade {{versao_atual}} {{nova_versao}}`

- Remove uma versão mantendo o código fonte:

`rvm uninstall {{versao}}`

- Remove uma versão e o código fonte:

`rvm remove {{versao}}`

- Exibe as dependências específicas para o seu sistema operacional:

`rvm requirements`
