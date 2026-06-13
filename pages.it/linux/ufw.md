# ufw

> Ufw (Uncomplicated Firewall) - Firewall Semplice.
> Frontend per `iptables` per semplificare la configurazione di un firewall.
> Maggiori informazioni: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- Accendi ufw:

`sudo ufw enable`

- Spegni ufw:

`sudo ufw disable`

- Mostra le regole di ufw, con i numeri corrispondenti:

`sudo ufw status numbered`

- Aperto al traffico in entrata sulla porta 5432, con un commento che identifica il servizio:

`sudo ufw allow 5432 comment "{{servizio}}"`

- Aperto solo al traffico TCP da 192.168.0.4 a qualsiasi indirizzo su questo host, sulla porta 22:

`sudo ufw allow proto tcp from 192.168.0.4 to any port 22`

- Blocchi traffico su porta 80 su questo host:

`sudo ufw deny 80`

- Nega tutto il traffico UDP alla porta 22:

`sudo ufw deny proto udp from any to any port 22`

- Elimina una regola particolare. Il numero della regola può essere trovato con "ufw status numbered":

`sudo ufw delete {{numero_della_regola}}`
