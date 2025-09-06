# top

> Mostra informações, em tempo real, sobre os processos em execução.
> Mais informações: <https://manned.org/top>.

- Inicia o `top`:

`top`

- Exibe apenas os processos ativos:

`top {{[-i|--idle-toggle]}}`

- Exibe os processos de um usuário específico:

`top {{[-u|--filter-only-euser]}} {{usuario}}`

- Ordena os processos por campo:

`top {{[-o|--sort-override]}} {{nome_do_campo}}`

- Mostra todas as threads de um dado processo:

`top {{[-Hp|--threads-show --pid]}} {{id_do_processo}}`

- Mostra apenas processos com determinados PID(s), informados em uma lista separada por vírgulas (Normalmente você não saberá os PIDs de cabeça. Este exemplo pega os PIDs a partir do nome de um processo):

`top {{[-p|--pid]}} $(pgrep {{[-d|--delimiter]}} ',' {{nome_do_processo}})`

- Mostra ajuda sobre comandos interativos:

`<?>`
