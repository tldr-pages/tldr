# networkctl

> Zapytaj o stan łączy sieciowych.
> Zarządzaj konfiguracją sieci za pomocą `systemd-networkd`.
> Więcej informacji: <https://www.freedesktop.org/software/systemd/man/networkctl.html>.

- Wyświetl listę istniejących łączy i ich status:

`networkctl list`

- Wyświetl ogólny status sieci:

`networkctl status`

- Włącz urządzenia sieciowe:

`networkctl up {{interfejs1 interfejs2 ...}}`

- Wyłącz urządzenia sieciowe:

`networkctl down {{interfejs1 interfejs2 ...}}`

- Odnów konfiguracje dynamiczne (np. adresy IP przydzielone przez serwer DHCP):

`networkctl renew {{interfejs1 interfejs2 ...}}`

- Przeładuj pliki konfiguracyjne (.netdev i .network):

`networkctl reload`

- Rekonfiguruj interfejsy sieciowe (jeżeli pliki konfiguracyjne były edytowane, najpierw uruchom `networkctl reload`):

`networkctl reconfigure {{interfejs1 interfejs2 ...}}`
