# certbot

> The Let's Encrypt Agent zum automatischen Erhalten und Erneuern von TLS-Zertifikaten.
> Nachfolger von `letsencrypt`.
> Mehr Informationen: <https://certbot.eff.org/docs/using.html>.

- Beziehen eines neuen Zertifikats über die webroot-Autorisierung, aber ohne dieses automatisch zu installieren:

`sudo certbot certonly --webroot --webroot-path {{pfad/zu/webroot}} --domain {{subdomain.beispiel.de}}`

- Beziehen eines neuen Zertifikats über die nginx-Autorisierung und automatische Installation des neuen Zertifikats:

`sudo certbot --nginx --domain {{subdomain.beispiel.de}}`

- Beziehen eines neuen Zertifikats über die apache-Autorisierung und automatische Installation des neuen Zertifikats:

`sudo certbot --apache --domain {{subdomain.beispiel.de}}`

- Erneuerung aller Let's Encrypt Zertifikate die in 30 Tagen or weniger auslaufen (nicht vergessen alle Server, die diese nutzen, neu zu starten):

`sudo certbot renew`

- Simulation der Zertifikatserneuerung, ohne diese zu speichern:

`sudo certbot --webroot --webroot-path {{pfad/zu/webroot}} --domain {{subdomain.beispiel.de}} --dry-run`

- Beziehen eines Test-Zertifikats:

`sudo certbot --webroot --webroot-path {{pfad/zu/webroot}} --domain {{subdomain.beispiel.de}} --test-cert`
