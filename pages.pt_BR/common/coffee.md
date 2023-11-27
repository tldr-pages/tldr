# coffee

> Executa scripts CoffeeScript ou os compila em JavaScript.
> Mais informações: <https://coffeescript.org#cli>.

- Executa um script:

`coffee {{caminho/para/arquivo.coffee}}`

- Compila para JavaScript e salva em um arquivo com o mesmo nome:

`coffee --compile {{caminho/para/arquivo.coffee}}`

- Compila para JavaScript e salva em um arquivo de saída indicado:

`coffee --compile {{caminho/para/arquivo.coffee}} --output {{caminho/para/arquivo.js}}`

- Inicia um REPL (shell interativo):

`coffee --interactive`

- Observa script para alterações e o executa novamente:

`coffee --watch {{caminho/para/arquivo.coffee}}`
