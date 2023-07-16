# autossh

> Executa, monitora e reinicia conexões SSH.
> Reconecta automaticamente para manter os túneis de redirecionamento de porta ativos. Aceita todas as flags do `ssh`.
> Mais informações: <https://www.harding.motd.ca/autossh>.

- Iniciar uma sessão SSH, reiniciando quando uma porta de monitoramento falhar em retornar dados:

`autossh -M {{porta_de_monitoramento}} "{{comando_ssh}}"`

- Redirecionar uma porta local para uma porta remota, reiniciando quando necessário:

`autossh -M {{porta_de_monitoramento}} -L {{porta_local}}:localhost:{{porta_remota}} {{usuário}}@{{host}}`

- Executar o `autossh` em segundo plano antes de executar o `ssh` e não abrir um shell remoto:

`autossh -f -M {{porta_de_monitoramento}} -N "{{comando_ssh}}"`

- Executar em segundo plano, sem porta de monitoramento, e em vez disso enviar pacotes de keep-alive SSH a cada 10 segundos para detectar falhas:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{comando_ssh}}"`

- Executar em segundo plano, sem porta de monitoramento e sem shell remoto, saindo se a redireção da porta falhar:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{porta_local}}:localhost:{{porta_remota}} {{usuário}}@{{host}}`

- Executar em segundo plano, registrando a saída de depuração do `autossh` e a saída detalhada do `ssh` em arquivos:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{caminho/para/arquivo_de_log_do_autossh.log}} autossh -f -M {{porta_de_monitoramento}} -v -E {{caminho/para/arquivo_de_log_do_ssh.log}} {{comando_ssh}}`
