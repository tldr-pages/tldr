# cupsctl

> Atualiza ou consulta o cupsd.conf de um server.
> Mais informações: <https://openprinting.github.io/cups/doc/man-cupsctl.html>.

- Exibe os valores de configuração atuais:

`cupsctl`

- Exibe os valores de configuração de um servidor específico:

`cupsctl -h {{servidor[:porta]}}`

- Ativa a criptografia na conexão ao scheduler:

`cupsctl -E`

- Ativa ou desativa o registro de depuração para o arquivo error_log:

`cupsctl {{--debug-logging|--no-debug-loging}}`

- Ativa ou desativa administração remota:

`cupsctl {{--remote-admin|--no-remote-admin}}`

- Exibe o estado atual do registro de depuração:

`cupsctl | grep '^_debug_logging' | awk -F= '{print $2}'`
