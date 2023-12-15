# cupsctl

> Atualiza ou consulta o cupsd.conf de um server.
> Mais informações: <https://www.cups.org/doc/man-cupsctl.html>.

- Exibir os valores de configuração atuais:

`cupsctl`

- Exibir os valores de configuração de um servidor específico:

`cupsctl -h {{servidor[:porta]}}`

- Exibir os valores de configuração atuais criptografando a conexão ao scheduler:

`cupsctl -E`

- Ativar ou desativar o registro de depuração para o arquivo error_log:

`cupsctl {{--debug-logging|--no-debug-loging}}`

- Ativar ou desativar a administração remota:

`cupsctl {{--remote-admin|--no-remote-admin}}`

- Exibir o estado atual do registro de depuração:

`cupsctl | grep '^_debug_logging' | awk -F= '{print $2}'`
