# certbot

> Agentul Let's Encrypt pentru obținerea și reînnoirea automată a certificatelor TLS.
> Succesor al `letsencrypt'.
> Mai multe informaţii: <https://certbot.eff.org/docs/using.html>

- Obțineți un nou certificat prin autorizarea webroot, dar nu îl instalați automat:

`sudo certbot certonly --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}}`

- Obțineți un nou certificat prin autorizarea nginx, instalând automat noul certificat:

`sudo certbot --nginx --domain {{subdomain.example.com}}`

- Obțineți un nou certificat prin autorizarea Apache, instalând automat noul certificat:

`sudo certbot --apache --domain {{subdomain.example.com}}`

- Reînnoiți toate certificatele Let's cript care expiră în 30 de zile sau mai puțin (nu uitați să reporniți orice servere care le utilizează după aceea):

`sudo certbot renew`

- Simulați obținerea unui nou certificat, dar nu salvați de fapt certificate noi pe disc:

`sudo certbot --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}} --dry-run`

- Obțineți în schimb un certificat de testare de încredere:

`sudo certbot --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}} --test-cert`
