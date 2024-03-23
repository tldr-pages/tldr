# npm

> Gerenciador de pacotes JavaScript e Node.js.
> Gerencia projetos Node.js e suas dependências de módulos.
> Mais informações: <https://www.npmjs.com>.

- Interativamente cria um arquivo `package.json`:

`npm init`

- Baixa todos os pacotes listados como dependências em `package.json`:

`npm install`

- Baixa uma versão específica de um pacote e o adiciona à lista de dependências em `package.json`:

`npm install {{pacote}}@{{versão}}`

- Baixa a última versão de um pacote e o adiciona à lista de dependências de desenvolvimento em `package.json`:

`npm install {{pacote}} --save-dev`

- Baixa a última versão de um pacote e o instala globalmente:

`npm install --global {{pacote}}`

- Desinstala um pacote e o remove da lista de dependências em `package.json`:

`npm uninstall {{pacote}}`

- Lista as dependências instaladas localmente:

`npm list`

- Lista os pacotes de nível superior instalados globalmente:

`npm list --global --depth={{0}}`
