# resolvectl

> Разрешать доменные имена, IPv4- и IPv6-адреса, DNS-записи ресурсов и сервисы.
> Просматривать и перенастраивать DNS-резолвер.
> Смотрите также: `dig`, `nslookup`, `host`.
> Больше информации: <https://www.freedesktop.org/software/systemd/man/latest/resolvectl.html>.

- Показать настройки DNS:

`resolvectl`

- Разрешить IPv4- и IPv6-адреса для одного или нескольких доменов:

`resolvectl query {{домен1 домен2 ...}}`

- Получить домен указанного IP-адреса:

`resolvectl query {{ip_адрес}}`

- Очистить все локальные кеши DNS:

`resolvectl flush-caches`

- Показать статистику DNS (транзакции, кеш и вердикты DNSSEC):

`resolvectl statistics`

- Получить MX-запись домена:

`resolvectl --legend {{no}} {{[-t|--type]}} {{MX}} query {{домен}}`

- Разрешить SRV-запись, например _xmpp-server._tcp gmail.com:

`resolvectl service _{{сервис}}._{{протокол}} {{имя}}`

- Получить TLS-ключ:

`resolvectl tlsa tcp {{домен}}:443`
