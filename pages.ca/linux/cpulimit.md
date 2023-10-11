# cpulimit

> Eina per limitar l'ús de la CPU en altres processos.
> Més informació: <http://cpulimit.sourceforge.net/>.

- Limita un procés existent amb PID 1234 perquè només utilitzi el 25% de CPU:

`cpulimit --pid {{1234}} --limit {{25%}}`

- Limita un programa existent per el seu nom d'execució:

`cpulimit --exe {{programa}} --limit {{25}}`

- Executa un programa determinat i limita el seu ús a només el 50% de la CPU:

`cpulimit --limit {{50}} -- {{programa argument1 argument2 ...}}`

- Executa un programa, limita l'ús de la CPU a 50% i executa cpulimit en segon pla:

`cpulimit --limit {{50}} --background -- {{programa}}`

- Mata el procés si l'ús de CPU del programa supera el 50%:

`cpulimit --limit 50 --kill -- {{programa}}`

- Regula el seu procés i els subprocessos perquè cap superi el 25% de CPU:

`cpulimit --limit {{25}} --monitor-forks -- {{programa}}`
