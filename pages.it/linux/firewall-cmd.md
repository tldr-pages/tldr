# firewall-cmd

> Il client a linea di comando firewalld.
> Visualizza e adatta lo stato di configurazione del firewall in esecuzione (runtime) o permanente.
> Maggiori informazioni: <https://firewalld.org/documentation/man-pages/firewall-cmd>.

- Visualizza tutte le zone e regole firewall disponibili nel loro stato di configurazione runtime:

`firewall-cmd --list-all-zones`

- Sposta permanentemente l'interfaccia nella zona block, bloccando effettivamente tutte le comunicazioni:

`firewall-cmd --permanent --zone {{block}} --change-interface {{enp1s0}}`

- Apre permanentemente la porta per un servizio nella zona specificata (come la porta 443 nella zona `public`):

`firewall-cmd --permanent --zone {{public}} --add-service {{https}}`

- Chiude permanentemente la porta per un servizio nella zona specificata (come la porta 80 nella zona `public`):

`firewall-cmd --permanent --zone {{public}} --remove-service {{http}}`

- Reindirizzare permanentemente una porta per i pacchetti in ingresso nella zona specificata (ad esempio dalla porta 443 alla 8443 nella zona `public`):

`firewall-cmd --permanent --zone {{public}} --add-rich-rule 'rule family "{{ipv4|ipv6}}" forward-port port "{{443}}" protocol "{{udp|tcp}}" to-port "{{8443}}"'`

- Ricarica firewalld per annullare tutte le modifiche temporanee (runtime) e applicare immediatamente la configurazione permanente:

`firewall-cmd --reload`

- Salva la configurazione runtime in quella permanente:

`firewall-cmd --runtime-to-permanent`

- Abilita la modalità di panico in caso di emergenza. Tutto il traffico viene bloccato, ogni connessione attiva viene terminata:

`firewall-cmd --panic-on`
