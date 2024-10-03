# at

> Executa comandos em um determinado momento.
> Mais informações: <https://manned.org/at.1>.

- Inicia o prompt `at` para que um novo conjunto de comandos seja agendado, pressione `Ctrl + D` para salvar e sair:

`at {{hh:mm}}`

- Executa os comandos e envia o resultado por e-mail utilizando algum programa de envio de e-mail local, por exemplo o Sendmail:

`at {{hh:mm}} -m`

- Executa um script em um determinado momento:

`at {{hh:mm}} -f {{caminho/para/arquivo}}`

- Mostra uma notificação de sistema às 23h em 18 de Fevereiro:

`echo "notify-send '{{Acorda!}}'" | at {{11pm}} {{Feb 18}}`
