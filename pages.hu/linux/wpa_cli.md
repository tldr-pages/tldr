# wpa_cli

> Wlan-interfészek hozzáadása és konfigurálása. További információ: <https://manned.org/wpa_cli>.

- Az elérhető hálózatok keresése:

`wpa_cli scan`

- A keresési eredmények megjelenítése:

`wpa_cli scan_results`

- Hálózat hozzáadása:

`wpa_cli add_network {{number}}`

- A hálózat SSID-jének beállítása:

`wpa_cli set_network {{number}} ssid "{{SSID}}"`

- Hálózat engedélyezése:

`wpa_cli enable_network {{number}}`

- Konfiguráció mentése:

`wpa_cli save_config`
