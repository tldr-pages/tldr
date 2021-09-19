# kill

> Envia um sinal para um processo, geralmente para finalizar o processo.
> Todos os sinais exceto pelo SIGKILL e SIGSTOP podem ser interceptados pelo processo para finalizar de forma limpa.
> Mais informações: <https://manned.org/kill>.

- Finaliza um programa usando o sinal default SIGTERM (terminate):

`kill {{id_do_processo}}`

- Lista todos os nomes dos sinais disponíveis (para serem usados sem o prefixo `SIG`):

`kill -l`

- Finaliza um processo em background:

`kill %{{id_do_processo}}`

- Finaliza um programa usando o sinal SIGHUP. Muitos daemons vão recarregar ao invés de finalizar:

`kill -{{1|HUP}} {{id_do_processo}}`

- Finaliza um programa usando o sinal SIGINT (interrupt). Isto é tipicamente iniciado pelo usuário ao pressionar `Ctrl + C`:

`kill -{{2|INT}} {{id_do_processo}}`

- Envia sinal para o sistema operacional para finalizar imediatamente o programa (quem não tem chance de capturar o sinal):

`kill -{{9|KILL}} {{id_do_processo}}`

- Envia sinal para o sistema operacional para pausar o programa até um sinal SIGCONT ("continue") seja recebido:

`kill -{{17|STOP}} {{id_do_processo}}`

- Envia um sinal `SIGUSR1` para todos os processos de um dado GID (group id):

`kill -{{SIGUSR1}} -{{id_do_grupo}}`
