# at

> Ferramenta para o agendamento de comandos.
> Resultados serão enviados para o e-mail dos usuários.
> Mais informações: <https://manned.org/at>.

- Inicia o daemon `atd`:

`systemctl start atd`

- Cria comandos interativamente e executa-os em 5 minutos (pressione `<Ctrl d>` quando acabar):

`at now + 5 minutes`

- Cria comandos interativamente e executa-os no horário específico:

`at {{hh:mm}}`

- Executa um comando da `stdin` (standard input) às 10:00 da manhã de hoje:

`echo "{{comando}}" | at 1000`

- Executa comandos de um dado arquivo na próxima terça:

`at -f {{caminho/para/arquivo}} 9:30 PM Tue`
