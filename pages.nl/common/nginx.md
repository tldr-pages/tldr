# nginx

> Nginx webserver.
> Meer informatie: <https://nginx.org/docs/switches.html>.

- Start de server met het standaard configuratiebestand:

`nginx`

- Start de server met een aangepast configuratiebestand:

`nginx -c {{configuratiebestand}}`

- Start de server met een prefix voor alle relatieve paden in het configuratiebestand:

`nginx -c {{configuratiebestand}} -p {{pad/naar/prefix}}`

- Test de configuratie zonder de actieve server te beïnvloeden:

`nginx -t`

- Herlaad de configuratie door een signaal te sturen zonder downtime:

`nginx -s reload`
