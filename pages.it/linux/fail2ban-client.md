# fail2ban-client

> Configurare e controllare il server fail2ban.
> Maggiori informazioni: <https://manned.org/fail2ban-client>.

- Ottiene lo stato corrente del servizio jail:

`fail2ban-client status {{jail}}`

- Rimuove l'IP specificato dalla lista ban del servizio jail:

`fail2ban-client set {{jail}} unbanip {{ip}}`

- Verifica che il server fail2ban sia attivo:

`fail2ban-client ping`
