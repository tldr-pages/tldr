# lpstat

> Exibe informações sobre o estado de impressoras.
> Mais informações: <https://manned.org/lpstat>.

- Lista impressoras presentes na máquina e se estão habilitadas para impressão:

`lpstat -p`

- Exibe a impressora padrão:

`lpstat -d`

- Exibe todas as informações de estado disponíveis:

`lpstat -t`

- Mostra uma lista de trabalhos de impressão que foram colocados na fila por um usuário específico:

`lpstat -u {{usuário}}`
