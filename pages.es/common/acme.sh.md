# acme.sh

> Shell script implementando el protocolo cliente ACME, una alternativa a `certbot`.
> Vea también `acme.sh dns`.
> Más información: <https://github.com/acmesh-official/acme.sh#2-just-issue-a-cert>.

- Emite un certificado usando el modo webroot:

`acme.sh --issue --domain {{ejemplo.com}} --webroot {{ruta/al/webroot}}`

- Emite un certificado para múltiples dominios utilizando el modo autónomo a través del puerto 80:

`acme.sh --issue --standalone --domain {{example.com}} --domain {{www.example.com}}`

- Emite un certificado en modo autónomo TLS utilizando el puerto 443:

`acme.sh --issue --alpn --domain {{example.com}}`

- Emite un certificado utilizando una configuración de Nginx operativa:

`acme.sh --issue --nginx --domain {{example.com}}`

- Emite un certificado utilizando una configuración de Apache operativa:

`acme.sh --issue --apache --domain {{example.com}}`

- Emite un certificado comodín (\*) utilizando un modo API DNS automático:

`acme.sh --issue --dns {{dns_cf}} --domain {{*.example.com}}`

- Instala archivos de certificado en las ubicaciones especificadas (útil para la renovación automática de certificados):

`acme.sh --install-cert -d {{example.com}} --key-file {{ruta/al/example.com.key}} --fullchain-file {{ruta/al/example.com.cer}} --reloadcmd "{{systemctl force-reload nginx}}"`
