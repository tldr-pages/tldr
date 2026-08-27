# acme.sh

> Script shell script que implementa o protocolo cliente ACME, ma alternativa para o `certbot`.
> Veja também: `acme.sh dns`.
> Mais informações: <https://github.com/acmesh-official/acme.sh#2-just-issue-a-cert>.

- Emite um certificado usando o modo webroot:

`acme.sh --issue {{[-d|--domain]}} {{example.com}} {{[-w|--webroot]}} /{{caminho/para/webroot}}`

- Emite um certificado para múltiplos domínios usando o modo standalone na porta 80:

`acme.sh --issue --standalone {{[-d|--domain]}} {{example.com}} {{[-d|--domain]}} {{www.example.com}}`

- Emite um certificado usando o modo standaline TLS na porta 443:

`acme.sh --issue --alpn {{[-d|--domain]}} {{example.com}}`

- Emite um certificado usando uma configuração válida `nginx`:

`acme.sh --issue --nginx {{[-d|--domain]}} {{example.com}}`

- Emite um certificado usando uma configuração válida Apache:

`acme.sh --issue --apache {{[-d|--domain]}} {{example.com}}`

- Emite um certificado wildcard (\*) usando o modo DNS_API automático:

`acme.sh --issue --dns {{dns_cf}} {{[-d|--domain]}} {{*.example.com}}`

- Instala os arquivos dos certificaods em um local específico (útil para renovação automática do certificado):

`acme.sh {{[-i|--install-cert]}} {{[-d|--domain]}} {{example.com}} --key-file /{{caminho/para/example.com.key}} --fullchain-file /{{caminho/para/example.com.cer}} --reloadcmd "{{systemctl force-reload nginx}}"`
