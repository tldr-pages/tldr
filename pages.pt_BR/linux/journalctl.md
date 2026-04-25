# journalctl

> Consulta o diário do systemd.
> Veja também: `dmesg`.
> Mais informações: <https://www.freedesktop.org/software/systemd/man/latest/journalctl.html>.

- Mostra as últimas `n` linhas e segue novas mensagens (similar ao `tail --follow` para o syslog tradicional):

`journalctl {{[-n|--lines]}} {{n}} {{[-f|--follow}]}`

- Mostra todas as mensagens com nível de prioridade 3 (erros) da inicialização anterior ao último desligamento:

`journalctl {{[-b|--boot]}} -1 {{[-p|--priority]}} 3`

- Mostra todas as mensagens de uma unidade específica:

`journalctl {{[-i|--unit]}} {{unidade}}`

- Mostra logs para uma certa unidade desde a última vez que foi iniciada:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID {{unidade}})`

- Filtra mensagens em um período de tempo (por data e hora ou marcadores como "yesterday"):

`journalctl {{[-S|--since]}} {{now|today|yesterday|tomorrow|...}} {{[-U|--until]}} "{{AAAA-MM-DD HH:MM:SS}}"`

- Mostra todas as mensagens de um processo específico:

`journalctl _PID={{pid}}`

- Mostra todas as mensagens de um executável específico:

`journalctl {{caminho/para/executável}}`

- Apaga logs no diário que tenham mais de 2 dias:

`journalctl --vaccum-time 2d`
