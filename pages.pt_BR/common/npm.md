# npm

> Gerenciador de pacotes JavaScript e Node.js.
> Gerencia projetos Node.js e suas dependências de módulos.
> Mais informações: <https://docs.npmjs.com/cli/npm/>.

- Cria um arquio `package.json` com os valores padrões (omita `--yes` para torná-lo interativo):

`npm init {{[-y|--yes]}}`

- Baixa todos os pacotes listados como dependências em `package.json`:

`npm {{[i|install]}}`

- Baixa uma versão específica de um pacote e o adiciona à lista de dependências em `package.json`:

`npm {{[i|install]}} {{pacote}}@{{versão}}`

- Baixa a última versão de um pacote e o adiciona à lista de dependências de desenvolvimento em `package.json`:

`npm {{[i|install]}} {{pacote}} {{[-D|--save-dev]}}`

- Baixa a última versão de um pacote e o instala globalmente:

`npm {{[i|install]}} {{pacote}} {{[-g|--global]}}`

- Desinstala um pacote e o remove da lista de dependências em `package.json`:

`npm {{[r|uninstall]}} {{pacote}}`

- Lista todas as dependências instaladas localmente:

`npm {{[ls|list]}}`

- Lista todos os pacotes de nível superior instalados globalmente:

`npm {{[ls|list]}} {{[-g|--global]}} --depth {{0}}`
