# certbot

> De Let's Encrypt Agent om automatisch TLS certificaten te verkrijgen en te vernieuwen.
> Opvolger van `letsencrypt`.
> Meer informatie: <https://eff-certbot.readthedocs.io/en/latest/using.html>.

- Verkrijg een nieuw certificaat via webroot autorisatie, maar installeer het certificaat niet automatisch:

`sudo certbot certonly --webroot {{[-w|--webroot-path]}} {{pad/naar/webroot}} {{[-d|--domain]}} {{subdomein.example.com}}`

- Verkrijg een nieuw certificaat via `nginx` autorisatie, installeer het nieuwe certificaat automatisch:

`sudo certbot --nginx {{[-d|--domain]}} {{subdomein.example.com}}`

- Verkrijg een nieuw certificaat via apache autorisatie, installeer het nieuwe certificaat automatisch:

`sudo certbot --apache {{[-d|--domain]}} {{subdomein.example.com}}`

- Vernieuw alle Let's Encrypt certificaten die binnen 30 dagen verlopen (vergeet achteraf niet alle servers te herstarten die deze gebruiken):

`sudo certbot renew`

- Simuleer het verkrijgen van een nieuw certificaat, zonder daadwerkelijk nieuwe certificaten op de schijf op te slaan:

`sudo certbot --webroot {{[-w|--webroot-path]}} {{pad/naar/webroot}} {{[-d|--domain]}} {{subdomein.example.com}} --dry-run`

- Verkrijg in plaats daarvan een onvertrouwd testcertificaat:

`sudo certbot --webroot {{[-w|--webroot-path]}} {{pad/naar/webroot}} {{[-d|--domain]}} {{subdomein.example.com}} --test-cert`
