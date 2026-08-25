# dig

> Utilità di lookup DNS.
> Vedi anche: `resolvectl`, `nslookup`, `host`.
> Maggiori informazioni: <https://manned.org/dig>.

- Mostra gli IP associati ad un hostname (record A):

`dig +short {{example.com}}`

- Mostra i mail server associati ad uno specifico dominio (record MX):

`dig +short {{example.com}} MX`

- Specifica un server DNS alternativo a cui fare richiesta:

`dig @{{8.8.8.8}} {{example.com}}`

- Esegui un lookup DNS inverso su di un indirizzo IP (record PTR):

`dig -x {{8.8.8.8}}`

- Trova i nameserver autoritativi per la zona e mostra i record SOA:

`dig +nssearch {{example.com}}`

- Esegui richieste iterative e mostra l'intero percorso per risolvere il dominio:

`dig +trace {{example.com}}`
