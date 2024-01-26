# bg

> Retomar a execução, em segundo plano, de processos que foram suspensos (e.g. utilizando `Ctrl + Z`).
> Mais informações: <https://manned.org/bg>.

- Retoma a execução, em segundo plano, do processo que foi suspenso mais recentemente:

`bg`

- Retoma um processo especifico (use `jobs -l` para obter o seu ID) e o executa em segundo plano:

`bg %{{id_processo}}`
