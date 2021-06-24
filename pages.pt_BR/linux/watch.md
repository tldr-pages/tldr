# watch

> Executa um comando repetidas vezes, e monitora a saída em tela cheia.

- Monitora arquivos no diretório atual:

`watch {{ls}}`

- Monitora espaço em disco e destaca as alterações:

`watch -d {{df}}`

- Monitora processos "node", atualizando a cada 3 segundos:

`watch -n {{3}} "{{ps aux | grep node}}"`
