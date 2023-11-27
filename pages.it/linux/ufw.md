# ufw

> Ufw (Uncomplicated Firewall) - Firewall Semplice.
> Frontend per `iptables` per semplificare la configurazione di un firewall.
> Maggiori informazioni: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- Accendi ufw:

`ufw enable`

- Spegni ufw:

`ufw disable`

- Mostra le regole di ufw, con i numeri corrispondenti:

`ufw status numbered`

- Aperto al traffico in entrata sulla porta 5432, con un commento che identifica il servizio:

`ufw allow {{5432}} comment "{{servizio}}"`

- Aperto solo al traffico TCP da 192.168.0.4 a qualsiasi indirizzo su questo host, sulla porta 22:

`ufw allow proto {{tcp}} from {{192.168.0.4}} to {{any}} port {{22}}`

- Blocchi traffico su porta 80 su questo host:

`ufw deny {{80}}`

- Nega tutto il traffico UDP alla porta 22:

`ufw deny proto {{udp}} from {{any}} to {{any}} port {{22}}`

- Elimina una regola particolare. Il numero della regola può essere trovato con "ufw status numbered":

`ufw delete {{numero_della_regola}}`
