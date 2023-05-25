# resolvectl

> Znajdź nazwy domen, adresy IPv4 i IPv6, rekordy zasobów DNS i usługi.
> Analizuj i rekonfiguruj resolwer DNS.
> Więcej informacji: <https://www.freedesktop.org/software/systemd/man/resolvectl.html>.

- Wyświetl ustawienia DNS:

`resolvectl status`

- Znajdź adresy IPv4 i IPv6 jednej lub więcej domen:

`resolvectl query {{domena1 domena2 ...}}`

- Znajdź domenę podanego adresu IP:

`resolvectl query {{adres_ip}}`

- Znajdź rekord MX podanej domeny:

`resolvectl --legend={{no}} --type={{MX}} query {{domena}}`

- Znajdź rekord SRV, na przykład _xmpp-server._tcp gmail.com:

`resolvectl service _{{usługa}}._{{protokół}} {{nazwa}}`

- Pobierz klucz publiczny z adresu email z rekordu DNS OPENPGPGKEY:

`resolvectl openpgp {{email}}`

- Znajdź klucz TLS:

`resolvectl tlsa tcp {{domena}}:443`
