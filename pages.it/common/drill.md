# drill

> Esegui varie query DNS.
> Maggiori informazioni: <https://manned.org/drill>.

- Mostra gli IP associati ad un hostname (record A):

`drill {{example.com}}`

- Cerca il/i server di posta associato/i a un dato nome di dominio (record MX):

`drill mx {{example.com}}`

- Recupera tutti i tipi di record per un dato dominio:

`drill any {{example.com}}`

- Specifica un server DNS alternativo da interrogare:

`drill {{example.com}} @{{8.8.8.8}}`

- Esegui un lookup DNS inverso su di un indirizzo IP (record PTR):

`drill -x {{8.8.8.8}}`

- Esegui un tracciamento DNSSEC dai root server fino al dominio:

`drill -TD {{example.com}}`

- Mostra record DNSKEY per un dominio:

`drill -s dnskey {{example.com}}`
