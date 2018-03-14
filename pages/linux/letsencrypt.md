# letsencrypt

> The Let's Encrypt Agent for automatically obtaining and renewing TLS certificates.

- Obtain a new certificate via webroot authorization:

`sudo letsencrypt --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}}`

- Obtain an untrusted test certificate instead:

`sudo letsencrypt --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}} --test-cert`

- Renew all Let's Encrypt certificates that expire soon (don't forget to restart any servers that use them afterwards):

`sudo letsencrypt renew`
