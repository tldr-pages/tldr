# kill

> Envia um sinal para um processo, geralmente para finalizar o processo 
> Todos os sinais exceto pelo SIGKILL e SIGSTOP podem ser interceptados pelo processo para finalizar de forma limpa.

- Finaliza um programa usando o sinal default SIGTERM (terminate):

`kill {{process_id}}`

- Lista todos os nomes dos sinais disponíveis (para serem usados sem o prefixo `SIG`):

`kill -l`

- Finaliza um processo em background:

`kill %{{job_id}}`

- Finaliza um programa usando o sinal SIGHUP. Muitos daemons vão recarregar ao invés de finalizar:

`kill -{{1|HUP}} {{process_id}}`

- Finaliza um programa usando o sinal SIGINT (interrupt). Isto é tipicamente iniciado pelo usuário ao pressionar `Ctrl + C`: 

`kill -{{2|INT}} {{process_id}}`

- Envia sinal para o sistema operacional para finalizar imediatamente o programa (quem não tem chance de capturar o sinal): 

`kill -{{9|KILL}} {{process_id}}`

- Envia sinal para o sistema operacional para pausar o programa até um sinal SIGCONT ("continue") seja recebido:

`kill -{{17|STOP}} {{process_id}}`

- Envia um sinal `SIGUSR1` para todos os processos de um dado GID (group id):

`kill -{{SIGUSR1}} -{{group_id}}`
