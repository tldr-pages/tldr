# fail2ban-client

> Configura e controla o servidor do fail2ban.
> Mais informações: <https://manned.org/fail2ban-client>.

- Obtém o status atual do serviço de uma jail:

`fail2ban-client status {{jail}}`

- Remove o IP especificado da lista de banimento de uma jail:

`fail2ban-client set {{jail}} unbanip {{ip_address}}`

- Verifica se o servidor do fail2ban está ativo:

`fail2ban-client ping`
