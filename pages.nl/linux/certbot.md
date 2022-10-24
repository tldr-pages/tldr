# certbot

> The Let's Encrypt Agent for automatically obtaining and renewing TLS certificates.
> Successor to `letsencrypt`.
> More information: <https://certbot.eff.org/docs/using.html>.

- Verkrijg een nieuw certificaat via webroot authorisatie, maar installeer het certificaat niet automatisch:

`sudo certbot certonly --webroot --webroot-path {{pad/naar/webroot}} --domain {{subdomein.voorbeeld.nl}}`

- Verkrijg een nieuw certificaat via nginx authorisatie, installeer het nieuwe certificaat automatisch:

`sudo certbot --nginx --domain {{subdomein.voorbeeld.nl}}`

- Verkrijg een nieuw certificaat via apache authorisatie, installeer het nieuwe certificaat automatisch:

`sudo certbot --apache --domain {{subdomein.voorbeeld.nl}}`

- Vernieuw alle Let's Encrypt certificaten die binnen 30 dagen verlopen (vergeet achteraf niet alle servers te herstarten die dit certificaat gebruiken):

`sudo certbot renew`

- Simuleer het verkrijgen van een nieuw certificaat, maar sla deze niet op, op een harde schijf:

`sudo certbot --webroot --webroot-path {{pad/naar/webroot}} --domain {{subdomein.voorbeeld.nl}} --dry-run`

- Verkrijg een onvertrouwd test certificaat:

`sudo certbot --webroot --webroot-path {{pad/naar/webroot}} --domain {{subdomein.voorbeeld.nl}} --test-cert`
