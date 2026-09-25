# networkctl

> Zapytaj o stan łączy sieciowych.
> Zarządzaj konfiguracją sieci za pomocą `systemd-networkd`.
> Więcej informacji: <https://www.freedesktop.org/software/systemd/man/latest/networkctl.html>.

- Wyświetl listę istniejących łączy i ich status:

`networkctl`

- Wyświetl ogólny status sieci:

`networkctl status`

- Włącz urządzenia sieciowe:

`sudo networkctl up {{interfejs1 interfejs2 ...}}`

- Wyłącz urządzenia sieciowe:

`sudo networkctl down {{interfejs1 interfejs2 ...}}`

- Odnów konfiguracje dynamiczne (np. adresy IP przydzielone przez serwer DHCP):

`sudo networkctl renew {{interfejs1 interfejs2 ...}}`

- Przeładuj pliki konfiguracyjne (`.netdev` i `.network`):

`sudo networkctl reload`

- Rekonfiguruj interfejsy sieciowe (jeżeli pliki konfiguracyjne były edytowane, najpierw uruchom `networkctl reload`):

`sudo networkctl reconfigure {{interfejs1 interfejs2 ...}}`
