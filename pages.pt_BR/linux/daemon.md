# daemon

> Roda processos em daemons.
> Mais informações: <https://manned.org/man/daemon.1>.

- Roda um comando como um daemon:

`daemon --name="{{nome}}" {{comando}}`

- Roda um comando como um daemon que será reiniciado se o comando falhar:

`daemon --name="{{nome}}" --respawn {{comando}}`

- Roda um comando como um daemon que será reiniciado se falar, com duas tentativas a cada 10 segundos:

`daemon --name="{{nome}}" --respawn --attempts=2 --delay=10 {{comando}}`

- Roda um comando como um daemon, gravando registros em um arquivo específico:

`daemon --name="{{nome}}" --errlog={{caminho/para/arquivo.log}} {{comando}}`

- Elimina um daemon (SIGTERM):

`daemon --name="{{nome}}" --stop`

- Lista os daemons:

`daemon --list`
