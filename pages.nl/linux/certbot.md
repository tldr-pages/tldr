# certbot

> De Let's Encrypt Agent om automatisch TLS certificaten te verkrijgen en te vernieuwen.
> Opvolger van `letsencrypt`.
> Meer informatie: <https://eff-certbot.readthedocs.io/en/latest/using.html>.

- Verkrijg een nieuw certificaat via webroot authorisatie, maar installeer het certificaat niet automatisch:

`sudo certbot certonly --webroot {{[-w|--webroot-path]}} {{pad/naar/webroot}} {{[-d|--domain]}} {{subdomein.example.com}}`

- Verkrijg een nieuw certificaat via nginx authorisatie, installeer het nieuwe certificaat automatisch:

`sudo certbot --nginx {{[-d|--domain]}} {{subdomein.example.com}}`

- Verkrijg een nieuw certificaat via apache authorisatie, installeer het nieuwe certificaat automatisch:

`sudo certbot --apache {{[-d|--domain]}} {{subdomein.example.com}}`

- Vernieuw alle Let's Encrypt certificaten die binnen 30 dagen verlopen (vergeet achteraf niet alle servers te herstarten die dit certificaat gebruiken):

`sudo certbot renew`

- Simuleer het verkrijgen van een nieuw certificaat, maar sla deze niet op, op een harde schijf:

`sudo certbot --webroot {{[-w|--webroot-path]}} {{pad/naar/webroot}} {{[-d|--domain]}} {{subdomein.example.com}} --dry-run`

- Verkrijg een onvertrouwd test certificaat:

`sudo certbot --webroot {{[-w|--webroot-path]}} {{pad/naar/webroot}} {{[-d|--domain]}} {{subdomein.example.com}} --test-cert`
