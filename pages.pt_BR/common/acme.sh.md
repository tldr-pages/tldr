# acme.sh

> Script shell script que implementa o protocolo cliente ACME, ma alternativa para o `certbot`.
> Veja também `acme.sh dns`.
> Mais informações: <https://github.com/acmesh-official/acme.sh>.

- Emite um certificado usando o modo webroot:

`acme.sh --issue --domain {{exemplo.com}} --webroot {{/caminho/para/webroot}}`

- Emite um certificado para múltiplos domínios usando o modo standalone na porta 80:

`acme.sh --issue --standalone --domain {{exemplo.com}} --domain {{www.exemplo.com}}`

- Emite um certificado usando o modo standaline TLS na porta 443:

`acme.sh --issue --alpn --domain {{exemplo.com}}`

- Emite um certificado usando uma configuração válida Nginx:

`acme.sh --issue --nginx --domain {{exemplo.com}}`

- Emite um certificado usando uma configuração válida Apache:

`acme.sh --issue --apache --domain {{exemplo.com}}`

- Emite um certificado wildcard (\*) usando o modo DNS_API automático:

`acme.sh --issue --dns {{dns_cf}} --domain {{*.exemplo.com}}`

- Instala os arquivos dos certificaods em um local específico (útil para renovação automática do certificado):

`acme.sh --install-cert -d {{exemplo.com}} --key-file {{/caminho/para/exemplo.com.key}} --fullchain-file {{/caminho/para/exemplo.com.cer}} --reloadcmd {{"systemctl force-reload nginx"}}`
