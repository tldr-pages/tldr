# lt

> Localtunnel expune localhost dvs. în lume pentru testare și partajare ușoară.
> Mai multe informaţii: <https://github.com/localtunnel/localtunnel>

- Porniți tunelul dintr-un anumit port:

`lt --port {{8000}}`

- Specificați serverul din amonte care face redirecționarea:

`lt --port {{8000}} --host {{host}}`

- Solicitați un subdomeniu specific:

`lt --port {{8000}} --subdomain {{subdomain}}`

- Imprimare informații de solicitare de bază:

`lt --port {{8000}} --print-requests`

- Deschideți adresa URL a tunelului în browserul web implicit:

`lt --port {{8000}} --open`
