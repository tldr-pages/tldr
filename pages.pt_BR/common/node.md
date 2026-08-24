# node

> Plataforma de JavaScript para o lado do Servidor (Node.js).
> Mais informações: <https://nodejs.org/docs/latest/api/cli.html#options>.

- Executa um arquivo JavaScript:

`node {{arquivo}}.js`

- Inicializa a REPL (shell interativa):

`node`

- Executa JavaScript, passando-o no comando:

`node {{[-e|--eval]}} "{{código}}"`

- Executa um arquivo JavaScript, imprimindo o resultado:

`node {{[-p|--print]}} "{{script}}"`

- Ativa o inspetor, pausando a execução até que um depurador seja conectado depois que o código-fonte for totalmente analisado:

`node --no-lazy --inspect-brk {{caminho/para/arquivo}}`
