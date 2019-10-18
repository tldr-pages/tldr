# at

> Ferramenta para o agendamento de comandos.
> O serviço atd (ou atrun) deve estar sendo executado para as atuais execuções.

- Executar comandos da standard input em 5 minutos (pressionar `Ctrl + D`quando acabar):

`at now + {{5}} minutes`

- Executar um comando da standard input às 10:00 da manhã de hoje:

`echo "{{./comando.sh}}" | at 1000`

- Executar comandos de um dado arquivo na próxima terça:

`at -f {{caminho/para/arquivo}} 9:30 PM Tue`
