# at

> Executa comandos em um determinado momento.

- Inicia o prompt `at` para que seja um novo conjunto de comandos agendados, pressione `Ctrl + D` para salvar e sair:

`at {{hh:mm:ss}}`

- Executa os comandos e envia o resultado utilizando por e-mail algum programa de envio de e-mail local, por exemplo o sendmail:

`at {{hh:mm:ss}} -m`

- Executa um script em um determinado momento:

`at {{hh:mm:ss}} -f {{path/to/file}}`
