# certbot

> O agente Let's Encrypt para obtenção e renovação de certificados TLS automaticamente.
> Sucessor do `letsencrypt`.

- Obtém um novo certificado via autorização webroot, porém não o instala automaticamente:

`sudo certbot certonly --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}}`

- Obtém um novo certificado via autorização nginx e o instala automaticamente:

`sudo certbot --nginx --domain {{subdomain.example.com}}`

- Obtém um novo certificado via autorização apache e o instala automaticamente:

`sudo certbot --apache --domain {{subdomain.example.com}}`

- Renova todos os certificados que expirarão em 30 dias ou menos (não esqueça de reiniciar todos os servidores que usam os certificados):

`sudo certbot renew`

- Simula a obtenção de um novo certificado, mas não o salva no disco:

`sudo certbot --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}} --dry-run`

- Obtém um certificado não confiável de teste:

`sudo certbot --webroot --webroot-path {{path/to/webroot}} --domain {{subdomain.example.com}} --test-cert`
