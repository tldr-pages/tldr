# caddy

> Um servidor web open source, pronto para empresas, com HTTPS automático, escrito em Go.
> Mais informações: <https://caddyserver.com>.

- Inicia Caddy em primeiro plano:

`caddy run`

- Inicia Caddy com um arquivo Caddy específico:

`caddy run --config {{caminho/para/arquivoCaddy}}`

- Inicia Caddy no plano de fundo:

`caddy start`

- Para um processo Caddy em plano de fundo:

`caddy stop`

- Executa um servidor de arquivo simples na porta especificada, com uma interface navegável:

`caddy file-server --listen :{{8000}} --browse`

- Executa um servidor proxy reverso:

`caddy reverse-proxy --from :{{80}} --to localhost:{{8000}}`
