# acme.sh

> Script del intérprete de comandos que implementa el protocolo cliente ACME, una alternativa a `certbot`.
> Vea también: `acme.sh dns`.
> Más información: <https://github.com/acmesh-official/acme.sh#2-just-issue-a-cert>.

- Emite un certificado utilizando el modo webroot:

`acme.sh --issue {{[-d|--domain]}} {{example.com}} {{[-w|--webroot]}} /{{ruta/a/webroot}}`

- Emite un certificado para varios dominios utilizando el modo autónomo con el puerto 80:

`acme.sh --issue --standalone {{[-d|--domain]}} {{example.com}} {{[-d|--domain]}} {{www.example.com}}`

- Emite un certificado utilizando el modo TLS autónomo con el puerto 443:

`acme.sh --issue --alpn {{[-d|--domain]}} {{example.com}}`

- Emite un certificado utilizando una configuración Nginx que está operativa:

`acme.sh --issue --nginx {{[-d|--domain]}} {{example.com}}`

- Emite un certificado utilizando una configuración Apache que está operativa:

`acme.sh --issue --apache {{[-d|--domain]}} {{example.com}}`

- Emite un certificado comodín (\*) utilizando un modo API DNS automático:

`acme.sh --issue --dns {{dns_cf}} {{[-d|--domain]}} {{*.example.com}}`

- Instala archivos de certificación en las ubicaciones especificadas (útil para la renovación automática de certificados):

`acme.sh {{[-i|--install-cert]}} {{[-d|--domain]}} {{example.com}} --key-file /{{ruta/a/example.com.key}} --fullchain-file /{{ruta/a/example.com.cer}} --reloadcmd "{{systemctl force-reload nginx}}"`
