# acme.sh --dns

> Использовать проверку DNS-01 для выпуска TLS-сертификата.
> Больше информации: <https://github.com/acmesh-official/acme.sh/wiki>.

- Выпустить сертификат, используя автоматический режим DNS API:

`acme.sh --issue --dns {{dns_gd}} --domain {{example.com}}`

- Выпустить wildcard-сертификат (отмеченный звёздочкой), используя автоматический режим DNS API:

`acme.sh --issue --dns {{dns_namesilo}} --domain {{example.com}} --domain {{*.example.com}}`

- Выпустить сертификат, используя режим DNS-алиаса (псевдонима):

`acme.sh --issue --dns {{dns_cf}} --domain {{example.com}} --challenge-alias {{alias-for-example-validation.com}}`

- Выпустить сертификат, отключив автоматический опрос DNS Cloudflare/Google после добавления DNS-записи и указав время ожидания в секундах:

`acme.sh --issue --dns {{dns_namecheap}} --domain {{example.com}} --dnssleep {{300}}`

- Выпустить сертификат, используя ручной режим DNS:

`acme.sh --issue --dns --domain {{example.com}} --yes-I-know-dns-manual-mode-enough-go-ahead-please`
