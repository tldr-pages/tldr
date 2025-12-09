# certbot

> The Let's Encrypt Agent zum automatischen Erhalten und Erneuern von TLS-Zertifikaten.
> Nachfolger von `letsencrypt`.
> Weitere Informationen: <https://eff-certbot.readthedocs.io/en/latest/using.html>.

- Beziehe ein neues Zertifikat über die webroot-Autorisierung, aber ohne dieses automatisch zu installieren:

`sudo certbot certonly --webroot {{[-w|--webroot-path]}} {{pfad/zu/webroot}} {{[-d|--domain]}} {{subdomain.beispiel.de}}`

- Beziehe ein neues Zertifikat über die nginx-Autorisierung und automatische Installation des neuen Zertifikats:

`sudo certbot --nginx {{[-d|--domain]}} {{subdomain.beispiel.de}}`

- Beziehe ein neues Zertifikat über die apache-Autorisierung und automatische Installation des neuen Zertifikats:

`sudo certbot --apache {{[-d|--domain]}} {{subdomain.beispiel.de}}`

- Erneuere alle Let's Encrypt Zertifikate die in 30 Tagen oder weniger auslaufen (nicht vergessen alle Server, die diese nutzen, neu zu starten):

`sudo certbot renew`

- Simuliere die Zertifikatserneuerung, ohne diese zu speichern:

`sudo certbot --webroot {{[-w|--webroot-path]}} {{pfad/zu/webroot}} {{[-d|--domain]}} {{subdomain.beispiel.de}} --dry-run`

- Beziehe ein Test-Zertifikat:

`sudo certbot --webroot {{[-w|--webroot-path]}} {{pfad/zu/webroot}} {{[-d|--domain]}} {{subdomain.beispiel.de}} --test-cert`
