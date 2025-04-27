# certbot

> The Let's Encrypt Agent for automatically obtaining and renewing TLS certificates.
> Successor to `letsencrypt`.
> More information: <https://eff-certbot.readthedocs.io/en/latest/using.html>.

- Obtain a new certificate via webroot authorization, but do not install it automatically:

`sudo certbot certonly --webroot {{[-w|--webroot-path]}} {{path/to/webroot}} {{[-d|--domain]}} {{subdomain.example.com}}`

- Obtain a new certificate via nginx authorization, installing the new certificate automatically:

`sudo certbot --nginx {{[-d|--domain]}} {{subdomain.example.com}}`

- Obtain a new certificate via apache authorization, installing the new certificate automatically:

`sudo certbot --apache {{[-d|--domain]}} {{subdomain.example.com}}`

- Renew all Let's Encrypt certificates that expire in 30 days or less (don't forget to restart any servers that use them afterwards):

`sudo certbot renew`

- Simulate the obtaining of a new certificate, but don't actually save any new certificates to disk:

`sudo certbot --webroot {{[-w|--webroot-path]}} {{path/to/webroot}} {{[-d|--domain]}} {{subdomain.example.com}} --dry-run`

- Obtain an untrusted test certificate instead:

`sudo certbot --webroot {{[-w|--webroot-path]}} {{path/to/webroot}} {{[-d|--domain]}} {{subdomain.example.com}} --test-cert`
