# watch

> Executa um comando repetidas vezes, e monitora a saída em tela cheia.
> Mais informações: <https://manned.org/watch>.

- Monitora arquivos no diretório atual:

`watch {{ls}}`

- Monitora espaço em disco e destaca as alterações:

`watch {{[-d|--differences]}} {{df}}`

- Monitora processos "node", atualizando a cada 3 segundos:

`watch {{[-n|--interval]}} {{3}} "{{ps aux | grep node}}"`

- Monitora o espaço em disco, e se ele mudar, para de monitorar:

`watch {{[-g|--chgexit]}} {{df}}`
