# top

> Mostra informações, em tempo real, sobre os processos em execução.
> Mais informações: <https://manned.org/top>.

- Inicia o `top`:

`top`

- Exibe apenas os processos ativos:

`top -i`

- Exibe os processos de um usuário específico:

`top -u {{usuario}}`

- Ordena os processos por campo:

`top -o {{nome_do_campo}}`

- Mostra todas as threads de um dado processo:

`top -Hp {{id_do_processo}}`

- Mostra apenas processos com determinados PID(s), informados em uma lista separada por vírgulas (Normalmente você não saberá os PIDs de cabeça. Este exemplo pega os PIDs a partir do nome de um processo):

`top -p $(pgrep -d ',' {{nome_do_processo}})`

- Mostra ajuda sobre comandos interativos:

`?`
