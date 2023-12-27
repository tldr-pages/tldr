# at

> Executa comandos em um determinado momento.
> Mais informações: <https://man.archlinux.org/man/at.1>.

- Inicia o prompt `at` para que um novo conjunto de comandos seja agendado, pressione `Ctrl + D` para salvar e sair:

`at {{hh:mm:ss}}`

- Executa os comandos e envia o resultado por e-mail utilizando algum programa de envio de e-mail local, por exemplo o sendmail:

`at {{hh:mm:ss}} -m`

- Executa um script em um determinado momento:

`at {{hh:mm:ss}} -f {{caminho_para_o_script}}`
