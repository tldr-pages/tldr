# acme.sh

> Скрипт оболочки, реализующий протокол ACME-клиента, альтернатива `certbot`.
> Смотрите также: `acme.sh dns`.
> Больше информации: <https://github.com/acmesh-official/acme.sh#2-just-issue-a-cert>.

- Выпустить сертификат, используя режим webroot:

`acme.sh --issue {{[-d|--domain]}} {{example.com}} {{[-w|--webroot]}} /{{путь/к/webroot}}`

- Выпустить сертификат для нескольких доменов в автономном (standalone) режиме через порт 80:

`acme.sh --issue --standalone {{[-d|--domain]}} {{example.com}} {{[-d|--domain]}} {{www.example.com}}`

- Выпустить сертификат в автономном режиме TLS через порт 443:

`acme.sh --issue --alpn {{[-d|--domain]}} {{example.com}}`

- Выпустить сертификат, используя текущую конфигурацию `nginx`:

`acme.sh --issue --nginx {{[-d|--domain]}} {{example.com}}`

- Выпустить сертификат, используя текущую конфигурацию Apache:

`acme.sh --issue --apache {{[-d|--domain]}} {{example.com}}`

- Выпустить wildcard-сертификат (\*), используя автоматический режим DNS API:

`acme.sh --issue --dns {{dns_cf}} {{[-d|--domain]}} {{*.example.com}}`

- Установить файлы сертификата в указанные места (полезно для автоматического продления сертификатов):

`acme.sh {{[-i|--install-cert]}} {{[-d|--domain]}} {{example.com}} --key-file /{{путь/к/example.com.key}} --fullchain-file /{{путь/к/example.com.cer}} --reloadcmd "{{systemctl force-reload nginx}}"`
