# kill

> Envia um sinal para um processo, geralmente para finalizar o processo.
> Todos os sinais exceto pelo `SIGKILL` e `SIGSTOP` podem ser interceptados pelo processo para finalizar de forma limpa.
> Mais informações: <https://manned.org/kill.1posix>.

- Finaliza um programa usando o sinal padrão `SIGTERM` (terminate):

`kill {{id_do_processo}}`

- Lista todos os nomes de sinais disponíveis (para serem usados sem o prefixo `SIG`):

`kill -l`

- Finaliza um programa usando o sinal `SIGHUP`. Muitos daemons vão recarregar ao invés de finalizar:

`kill {{[-1|-SIGHUP]}} {{id_do_processo}}`

- Finaliza um programa usando o sinal `SIGINT` (interrupt). Isto é tipicamente iniciado pelo usuário ao pressionar `<Ctrl c>`:

`kill {{[-2|-SIGINT]}} {{id_do_processo}}`

- Envia sinal para o sistema operacional para finalizar imediatamente o programa (que não tem chance de capturar o sinal):

`kill {{[-9|-SIGKILL]}} {{id_do_processo}}`

- Envia sinal para o sistema operacional para pausar o programa até que um sinal `SIGCONT` ("continue") seja recebido:

`kill {{[-STOP|-SIGSTOP]}} {{id_do_processo}}`

- Envia um sinal `SIGUSR1` para todos os processos de um dado GID (group id):

`kill {{[-USR1|-SIGUSR1]}} -{{id_do_grupo}}`
