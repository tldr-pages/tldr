# daemon

> Roda processos em daemons.
> Mais informações: <https://manned.org/daemon.1>.

- Roda um comando como um daemon:

`daemon {{[-n|--name]}} "{{nome}}" {{comando}}`

- Roda um comando como um daemon que será reiniciado se o comando falhar:

`daemon {{[-n|--name]}} "{{nome}}" {{[-r|--respawn]}} {{comando}}`

- Roda um comando como um daemon que será reiniciado se falar, com duas tentativas a cada 10 segundos:

`daemon {{[-n|--name]}} "{{nome}}" {{[-r|--respawn]}} {{[-A|--attempts]}} 2 {{[-L|--delay]}} 10 {{comando}}`

- Roda um comando como um daemon, gravando registros em um arquivo específico:

`daemon {{[-n|--name]}} "{{nome}}" {{[-l|--errlog]}} {{caminho/para/arquivo.log}} {{comando}}`

- Elimina um daemon (SIGTERM):

`daemon {{[-n|--name]}} "{{nome}}" --stop`

- Lista os daemons:

`daemon --list`
