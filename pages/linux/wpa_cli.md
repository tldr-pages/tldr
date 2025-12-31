# wpa_cli

> Add and configure Wi-Fi interfaces.
> More information: <https://manned.org/wpa_cli>.

- Scan for available networks:

`sudo wpa_cli scan`

- Show scan results:

`sudo wpa_cli scan_results`

- Add a network:

`sudo wpa_cli {{[add_n|add_network]}} {{number}}`

- Set a network's SSID:

`sudo wpa_cli {{[set_n|set_network]}} {{number}} ssid "{{SSID}}"`

- Enable network:

`sudo wpa_cli {{[en|enable_network]}} {{number}}`

- Save config:

`sudo wpa_cli {{[sa|save_config]}}`
