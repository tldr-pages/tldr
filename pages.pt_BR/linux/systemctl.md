# systemctl

> Controla o sistema systemd e o gerenciador de serviços.
> Mais informações: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Mostra todos os serviços em execução:

`systemctl status`

- Lista unidades com falha:

`systemctl --failed`

- Inicia/Para/Reinicia/Recarrega um serviço:

`systemctl {{start|stop|restart|reload}} {{unidade}}`

- Mostra o status de uma unidade:

`systemctl status {{unidade}}`

- Ativa/Desativa uma unidade a ser iniciada na inicialização:

`systemctl {{enable|disable}} {{unidade}}`

- Mascara/Desmascara uma unidade para impedir ativação e ativação manual:

`systemctl {{mask|unmask}} {{unidade}}`

- Recarrega o systemd, verificando por unidades novas ou alteradas:

`systemctl daemon-reload`

- Verifica se uma unidades está ativada:

`systemctl is-enabled {{unidade}}`
