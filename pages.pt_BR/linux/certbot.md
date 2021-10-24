# certbot

> O agente da Let's Encrypt para obtenção e renovação de certificados TLS automaticamente.
> Sucessor do `letsencrypt`.
> Mais informações: <https://certbot.eff.org/docs/using.html>.

- Obter um novo certificado via autorização webroot, porém sem instalá-lo automaticamente:

`sudo certbot certonly --webroot --webroot-path {{caminho_para_webroot}} --domain {{subdominio.dominio.com}}`

- Obter um novo certificado via autorização nginx e instalá-lo automaticamente:

`sudo certbot --nginx --domain {{subdominio.dominio.com}}`

- Obter um novo certificado via autorização apache e instalá-lo automaticamente:

`sudo certbot --apache --domain {{subdominio.dominio.com}}`

- Renovar todos os certificados que expirarão em 30 dias ou menos (não esqueça de reiniciar todos os servidores que usam os certificados):

`sudo certbot renew`

- Simular a obtenção de um novo certificado, porém sem salvá-lo no disco rígido:

`sudo certbot --webroot --webroot-path {{caminho_para_webroot}} --domain {{subdominio.dominio.com}} --dry-run`

- Obter um certificado não confiável para testes:

`sudo certbot --webroot --webroot-path {{caminho_para_webroot}} --domain {{subdominio.dominio.com}} --test-cert`
