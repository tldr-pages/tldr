# wpa_cli

> Adăugați și configurați interfețe wlan.

- Scanare pentru reţele disponibile:

`wpa_cli scan`

- Arată rezultatele scanării:

`wpa_cli scan_results`

- Adaugă o reţea:

`wpa_cli add_network {{number}}`

- Setați SSID-ul unei rețele:

`wpa_cli set_network {{number}} ssid "{{SSID}}"`

- Activează rețeaua:

`wpa_cli enable_network {{number}}`

- Salvați configurația:

`wpa_cli save_config`
