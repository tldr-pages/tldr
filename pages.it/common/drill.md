# drill

> Esegui varie query DNS.
> Maggiori informazioni: <https://manned.org/drill>.

- Mostra gli IP associati ad un hostname (record A):

`drill {{esempio.com}}`

- Lookup the mail server(s) associated with a given domain name (MX record):

`drill mx {{esempio.com}}`

- Recupera tutti i tipi di record per un dato dominio:

`drill any {{esempio.com}}`

- Specifica un server DNS alternativo da interrogare:

`drill {{esempio.com}} @{{8.8.8.8}}`

- Esegui un lookup DNS inverso su di un indirizzo IP (record PTR):

`drill -x {{8.8.8.8}}`

- Esegui un tracciamento DNSSEC dai root server fino al dominio:

`drill -TD {{esempio.com}}`

- Mostra record DNSKEY per un dominio:

`drill -s dnskey {{esempio.com}}`
