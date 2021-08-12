# host

> Căutare server de nume de domeniu.

- Lookup A, AAAA și MX înregistrări ale unui domeniu:

`host {{domain}}`

- Caută un câmp (CNAME, TXT,...) al unui domeniu:

`host -t {{field}} {{domain}}`

- Căutare inversă un IP:

`host {{ip_address}}`

- Specificați un server DNS alternativ pentru interogare:

`host {{domain}} {{8.8.8.8}}`
