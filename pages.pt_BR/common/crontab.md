# crontab

> Agenda tarefas cron para serem executadas em um intervalo de tempo para o usuário atual.
> Mais informações: <https://manned.org/crontab>.

- Edita o arquivo crontab para o usuário atual:

`crontab -e`

- Edita o arquivo crontab para um usuário específico:

`sudo crontab -e -u {{usuário}}`

- Substitui o crontab atual pelo conteúdo do arquivo fornecido:

`crontab {{caminho/para/arquivo}}`

- Exibe uma lista de tarefas cron existentes para o usuário atual:

`crontab -l`

- Remove todos as tarefas de cron do usuário atual:

`crontab -r`

- Exemplo de tarefa executada às 10:00 todos os dias (* significa qualquer valor):

`0 10 * * * {{comando_para_executar}}`

- Exemplo de entrada do crontab, que executa um comando a cada 10 minutos:

`*/10 * * * * {{comando_para_executar}}`

- Exemplo de entrada do crontab, que executa um determinado script às 02:30 todas as sextas-feiras:

`30 2 * * Fri {{/caminho/absoluto/para/script.sh}}`
