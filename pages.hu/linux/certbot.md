# certbot

> A Let's Encrypt Agent a TLS tanúsítványok automatikus beszerzésére és megújítására. A `letsencrypt` utódja. További információ: <https://certbot.eff.org/docs/using.html>.

- Új tanúsítvány beszerzése a webroot engedélyezésen keresztül, de nem telepíti automatikusan:

`sudo certbot certonly --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}}`

- Új tanúsítvány beszerzése az nginx engedélyezésén keresztül, az új tanúsítvány automatikus telepítése:

`sudo certbot --nginx --domain {{subdomain.example.com}}`

- Új tanúsítvány beszerzése apache-engedélyezéssel, az új tanúsítvány automatikus telepítése:

`sudo certbot --apache --domain {{subdomain.example.com}}`

- Újítsa meg az összes Let's Encrypt tanúsítványt, amely 30 napon belül vagy annál rövidebb időn belül lejár (ne felejtse el újraindítani az ezeket használó szervereket ezután):

`sudo certbot renew`

- Szimulálja az új tanúsítvány megszerzését, de valójában ne mentsen új tanúsítványokat a lemezre:

`sudo certbot --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}} --dry-run`

- Ehelyett szerezzen be egy nem megbízható teszt-tanúsítványt:

`sudo certbot --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}} --test-cert`
