# while

> Loop simples da shell.

- Lê a entrada default (stdin) e realiza uma ação a cada linha:

`while read line; do echo "$line"; done`

- Executa um comando para sempre a cada segundo:

`while :; do {{comando}}; sleep 1; done`
