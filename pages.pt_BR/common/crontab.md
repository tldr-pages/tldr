# crontab

> Agenda tarefas (jobs) do cron para rodarem em um intervalo de tempo para o usuário atual.
> Mais informações: <https://crontab.guru/>.

- Edita o arquivo crontab para o usuário atual:

`crontab -e`

- Edita o arquivo crontab para um usuário específico:

`sudo crontab -e -u {{usuário}}`

- Substitui o conteúdo do crontab pelo conteúdo do arquivo listado:

`crontab {{caminho/para/o/arquivo}}`

- Lista as tarefas (jobs) cron existentes para o usuário atual:

`crontab -l`

- Remove todas as tarefas (jobs) cron para o usuário atual:

`crontab -r`

- Tarefa de exemplo que executa todo dia às 10:00 (* corresponde a qualquer valor):

`0 10 * * * {{comando_para_executar}}`

- Tarefa de exemplo que roda um comando a cada 10 minutos:

`*/10 * * * * {{comando_para_executar}}`

- Tarefa de exemplo que roda um script toda Sexta-Feira (Friday/Fri) às 02:30:

`30 2 * * Fri {{/absolute/path/to/script.sh}}`
