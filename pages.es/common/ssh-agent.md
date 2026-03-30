# ssh-agent

> Inicia un proceso SSH Agent.
> Nota: Un SSH Agent mantiene las claves SSH descifradas en memoria hasta que se eliminan o se mata el proceso.
> Ver también: `ssh-add`.
> Más información: <https://man.openbsd.org/ssh-agent>.

- Inicia un SSH Agent para el shell actual:

`eval $(ssh-agent)`

- Termina el agente en ejecución actual:

`ssh-agent -k`
