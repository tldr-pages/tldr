# netstat

> Mostra le connessioni TCP attive, le porte alla quale il computer e' in ascolto, statistiche dell'adattatore di rete, la tabella di routing IP, statistiche IPv4 e statistiche IPv6.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/netstat>.

- Mostra le connessioni TCP attive:

`netstat`

- Mostra tutte le connessioni TCP attive e le porte TCP e UDP sulla quale il computer è in ascolto:

`netstat -a`

- Mostra statistiche dell'adattatore di rete, come i numeri di bytes e pacchetti inviati e ricevuti:

`netstat -e`

- Mostra connessioni TCP attive e esprimi indirizzi e numeri di porta in formato numerico:

`netstat -n`

- Mostra connessioni TCP attive e includi l'identificatore di processo (PID) per ogni connessione:

`netstat -o`

- Mostra il contenuto della tabella di routing IP:

`netstat -r`

- Mostra statistiche divise per protocollo:

`netstat -s`

- Mostra la lista delle porte attualmente aperte ed i relativi indirizzi IP:

`netstat -an`
