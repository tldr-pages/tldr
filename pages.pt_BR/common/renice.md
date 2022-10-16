# renice

> Altera a prioridade/agradabilidade de agendamento de um ou mais processos em execução.
> Os valores de agradabilidade variam de -20 (mais favorável ao processo) a 19 (menos favorável ao processo).
> Mais informações: <https://manned.org/renice>.

- Altera a prioridade de um processo em execução:

`renice -n {{niceness_value}} -p {{pid}}`

- Altera a prioridade de todos os processos pertencentes a um usuário:

`renice -n {{niceness_value}} -u {{user}}`

- Altera a prioridade de todos os processos que pertencem a um grupo de processos:

`renice -n {{niceness_value}} --pgrp {{process_group}}`
