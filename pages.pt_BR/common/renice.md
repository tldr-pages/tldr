# renice

> Altera a prioridade/agradabilidade de agendamento de um ou mais processos em execução.
> Os valores de agradabilidade variam de -20 (mais favorável ao processo) a 19 (menos favorável ao processo).
> Mais informações: <https://manned.org/renice>.

- Altera a prioridade de um [p]rocesso em execução:

`renice -n {{3}} -p {{pid}}`

- Altera a prioridade de todos os processos pertencentes a um [u]suário:

`renice -n {{-4}} -u {{nome_do_usuario}}`

- Altera a prioridade de todos os processos que pertencem a um [g]rupo de processos:

`renice -n {{5}} -g {{grupo_de_processos}}`
