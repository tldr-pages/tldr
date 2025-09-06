# ssh-agent

> Iniciar um processo do Agente SSH.
> Um Agente SSH mantém as chaves SSH descriptografadas na memória até serem removidas ou o processo ser encerrado.
> Veja também `ssh-add`, que pode adicionar e gerenciar chaves mantidas por um Agente SSH.
> Mais informações: <https://man.openbsd.org/ssh-agent>.

- Inicia um Agente SSH para o shell atual:

`eval $(ssh-agent)`

- Encerra o Agente em execução atualmente:

`ssh-agent -k`
