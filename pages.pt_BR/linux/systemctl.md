# systemctl

> Controla o sistema systemd e o gerenciador de serviços.
> Mais informações: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Mostra todos os serviços em execução:

`systemctl status`

- Lista unidades com falha:

`systemctl --failed`

- Inicia/Para/Reinicia/Recarrega o estado um serviço:

`systemctl {{start|stop|restart|reload}} {{unidade}}`

- Ativa/Desativa uma unidade a ser iniciada na inicialização:

`systemctl {{enable|disable}} {{unidade}}`

- Recarrega o systemd, verificando por unidades novas ou alteradas:

`systemctl daemon-reload`

- Verifica se uma unidade está ativada/ativa/em falha:

`systemctl {{is-active|is-enabled|isfailed}} {{unidade}}`

- Lista todos as unidades de serviço/socket/auto-montável filtrando por estado executando/falhou:

`systemctl list-units {{[-t|--type]}} {{service|socket|automount}} --state {{failed|running}}`

- Mostra o conteúdo e o caminho absoluto do arquivo de uma unidade:

`systemctl cat {{unidade}}`
